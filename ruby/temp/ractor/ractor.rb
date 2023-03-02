WORDS = Ractor.make_shareable File.readlines('/usr/share/dict/words').map(&:chomp).map(&:downcase).sort

def try
  File.readlines(__dir__ + '/compar.c').each{|line|
    line.split.map(&:downcase).select { |text|
      WORDS.include? text
    }
  }
end

Warning[:experimental] = false

require 'benchmark'

Benchmark.bm{|x|
  x.report{
    4.times{try}
  }
  x.report{
    4.times.maprb{
      Ractor.new{ try }
    }.each(&:take)
  }
}
