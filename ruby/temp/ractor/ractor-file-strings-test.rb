#!/usr/bin/env ruby

# Benchmarks performance of processing a CPU load with one ractor and multiple ractors, and compares the results.
#
# Two measurements will be done; one with 1 ractor, and the other with the number of ractors set to the number of CPU's.
# The order of the two tests is randomized.
#
# Input consists of files on the filesystem. By default, all files in the current directory and below will be processed.
#
# This can be overridden:
#
# ARGV[0] - base directory from which to navigate downward, inclusive of the base directory
# ARGV[1] - file mask for use as parameter to Unix `find` command's `name` parameter
#
# For each file meeting the filter criteria, the Unix `strings` command is run to find that file's character sequences resembling strings.
# Then a set of "words" is created containing only those strings that are found in the system's `words` dictionary.
# That set is then merged into the ractor's all-file-scope set of words.
#
# When all ractors are finished, each ractor's set of words is merged into a global one, and the result saved to a file
# whose name will include the number of ractors used, e.g. `ractor-words-1.txt` and `ractor-words-24.txt`.
# A difference between those files (not likely) indicates an error in the run that is probably not related to ractors.
#
# The test has no real use other than exercising the CPU's, and performance improvements have deliberately not been pursued.
#
# The `amazing_print` gem is used to nicely output some information, and needs to be `gem install`ed.

require 'amazing_print'
require 'benchmark'
require 'etc'
require 'ostruct'
require 'prettyprint'
require 'set'
require 'shellwords'
require 'json'
require 'yaml'


Warning[:experimental] = false if defined? Warning[]  # disable ractor experimental warning

# ==================================================================================================
# An instance of this file processor class is created for each file-processing ractor.
# ==================================================================================================
class RactorFileProcessor

  attr_reader :dictionary_words, :name

  def initialize(name, dictionary_words)
    @dictionary_words = dictionary_words
    @name = name
  end

  def process_file(filespec)
    file_lines(filespec).each_with_object(Set.new) do |line, file_words|
      line_words(line).each { |word| file_words << word }
    end
  end

  private def word?(string)
    dictionary_words.include?(string)
  end

  private def strip_punctuation(string)
    string.gsub(/[[:punct:]]/, ' ')
  end

  private def file_lines(filespec)
    command = "strings #{Shellwords.escape(filespec)}"
    strip_punctuation(`#{command}`).split("\n")
  end

  private def line_words(line)
    line.split.map(&:downcase).select { |text| word?(text) }
  end
end


# ==================================================================================================
# This class defines the behavior of the processor ractor (i.e. provides the body for its `new` block)
# ==================================================================================================
class FileProcessorRactorBody

  def self.call; new.call; end

  attr_reader :dictionary_words, :name, :found_words, :processor, :start_time, :yielder

  def call
    set_up_vars

    loop do
      filespec = yielder.take
      next unless filespec_valid?(filespec)
      found_words.merge(processor.process_file(filespec))
    end

    printf("Ractor %-12s duration (secs): %.5f\n", name, (Time.now - start_time).round(5))
    found_words
  end


  private def filespec_valid?(filespec)
    filespec.is_a?(String) && filespec.length > 0
  end


  private def set_up_vars
    @name = Ractor.receive
    @dictionary_words = Ractor.receive
    @yielder = Ractor.receive
    @found_words = Set.new
    @processor = RactorFileProcessor.new(name, dictionary_words)
    @start_time = Time.now
  end
end


# ====================================================================================================
# This class defines the behavior of the processor ractor (i.e. provides the body for its `new` block)
# ====================================================================================================
class FilespecYieldingRactorBody

  def self.call; new.call; end

  attr_reader :filespecs, :file_count, :report_interval_secs, :time_to_report_progress

  def call
    setup_vars
    puts # make some vertical whitespace to offset the ractor warning
    report_progress(0)

    filespecs.each_with_index do |filespec, file_num|
      Ractor.yield(filespec)
      report_progress(file_num)
    end
    go_to_start_of_terminal_line
    puts "Finished sending filespecs to ractors. They may take a while to finish processing.\n\n"
  end

  private def go_to_start_of_terminal_line
    print("\e[G")
  end

  private def setup_vars
    @filespecs = Ractor.receive
    @report_interval_secs = 1
    @time_to_report_progress = Time.now - 100 # some time in the past
    @file_count = filespecs.size
  end

  private def report_progress(file_num)
    if Time.now > time_to_report_progress
      percent_complete = (100.0 * file_num / file_count).round(2)
      message = sprintf("%05.2f%% complete [%6d / %6d]", percent_complete, file_num, file_count)
      go_to_start_of_terminal_line
      print message
      @time_to_report_progress = Time.now + report_interval_secs
    end
  end
end


# ==================================================================================================
# Run the test with the specified number of ractors.
# ==================================================================================================
class TestRun

  def self.call(all_filespecs, ractor_count); self.new(all_filespecs, ractor_count).call; end

  attr_reader :all_filespecs, :ractor_count

  def initialize(all_filespecs, ractor_count)
    @all_filespecs = all_filespecs
    @ractor_count = ractor_count
  end

  def call
    puts "\n\n#{'-' * 100}\nUsing #{ractor_count} ractor(s):"
    ractors = create_and_populate_ractors
    all_words = nil
    benchmark = benchmark_to_hash(Benchmark.measure { all_words = collate_ractor_results(ractors) })
    write_results(all_words, benchmark)
    benchmark
  end


  private def write_results(all_words, benchmark)
    words_filespec = "ractor-words-#{ractor_count}.txt"
    File.write(words_filespec, all_words.to_a.sort.join("\n"))
    puts "\nFinished. Words are in #{words_filespec}, log files are *.log."
    puts "Using #{ractor_count} ractor(s):"
    ap benchmark
    puts "\nJSON:"
    puts benchmark.to_json
    puts "\nYAML:"
    puts benchmark.to_yaml
  end


  private def collate_ractor_results(ractors)
    ractors.inject(Set.new) do |all_words, ractor|
      all_words | ractor.take
    end
  end


  private def create_filespec_yielding_ractor
    ractor = Ractor.new(name: 'FilespecYielder') { FilespecYieldingRactorBody.call }
    ractor.send(all_filespecs)
    ractor
  end


  private def create_and_populate_ractors
    filespec_yielder = create_filespec_yielding_ractor
    dictionary_words = File.readlines('/usr/share/dict/words').map(&:chomp).map(&:downcase).sort
    (0...ractor_count).map do |index|
      name = "ractor-#{index}"
      ractor = Ractor.new(name: name) { FileProcessorRactorBody.call }
      ractor.send(name)
      ractor.send(dictionary_words)
      ractor.send(filespec_yielder)
    end
  end


  private def benchmark_to_hash(bm)
    {
      user: bm.utime.round(3),
      system: bm.stime.round(3),
      total: bm.total.round(3),
      real: bm.real.round(3)
    }
  end
end


# ==================================================================================================
# Main Entry Point of the Script (Main#call)
# ==================================================================================================
class Main

  def call
    check_for_ruby_3
    Ractor.new {}
    check_arg_count
    all_filespecs = find_all_filespecs

    do_1_cpu_first = [true, false].sample
    if do_1_cpu_first
      benchmark_1_cpu = TestRun.call(all_filespecs, 1)
      benchmark_all_cpus = TestRun.call(all_filespecs, processor_count)
    else
      benchmark_all_cpus = TestRun.call(all_filespecs, processor_count)
      benchmark_1_cpu = TestRun.call(all_filespecs, 1)
    end

    write_summary_results(benchmark_1_cpu, benchmark_all_cpus)
  end


  private def write_summary_results(benchmark_1, benchmark_all)
    b1 = OpenStruct.new(benchmark_1)
    bn = OpenStruct.new(benchmark_all)
    headings = ["", "1 CPU", "#{processor_count} CPU's", "Factor", "1 / Factor"]
    format_string = "%-12.12s %16.5f %16.5f %16.5f %16.5f\n"
    headings_format_string = "%12s %16s %16s %16s %16s\n"

    puts "\n\n#{'=' * 100}\nSummary Results:\n#{'=' * 100}\n\n"
    printf(headings_format_string, *headings)
    puts('-' * 80)
    printf(format_string, 'User',   b1.user,   bn.user,   bn.user   / b1.user,   b1.user   / bn.user)
    printf(format_string, 'System', b1.system, bn.system, bn.system / b1.system, b1.system / bn.system)
    printf(format_string, 'Total',  b1.total,  bn.total,  bn.total  / b1.total,  b1.total  / bn.total)
    printf(format_string, 'Real',   b1.real,   bn.real,   bn.real   / b1.real,   b1.real   / bn.real)
  end


  private def processor_count
    Etc.nprocessors
  end

  private def check_arg_count
    if ARGV.length > 2
      puts "Syntax is ractor [base_directory] [filemask], and filemask must be quoted so that the shell does not expand it."
      exit -1
    end
  end


  private def find_all_filespecs
    file_mask = ARGV[1] ? %Q{-name '#{ARGV[1]}'} : ''
    base_dir = ARGV[0] || '.'
    command = "find -L #{base_dir} -type f #{file_mask} -print"
    puts "Running the following command to find all filespecs to process: #{command}"
    filespecs = `#{command}`.split("\n").map(&:freeze)
    puts "Found #{filespecs.size} files."
    filespecs
  end


  private def init_ractor_count
    specified_as_env_var = !!ENV['RACTOR_COUNT']
    @ractor_count = specified_as_env_var ? ENV['RACTOR_COUNT'].to_i : Etc.nprocessors

    raise "Ractor count must > 0." unless @ractor_count > 0

    unless specified_as_env_var
      puts "Using the number of CPU's (#{@ractor_count}) as the number of ractors.\n" \
         + "You can also optionally specify the number of ractors to use with the environment variable RACTOR_COUNT."
    end
  end

  private def check_for_ruby_3
    unless RUBY_VERSION.split('.').first.to_i >= 3
      puts "This script requires Ruby version 3 or later."
      exit -1
    end
  end

end

# ==================================================================================================

Main.new.call
