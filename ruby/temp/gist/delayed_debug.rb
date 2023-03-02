# Non blocking delayed debugger for production
# https://gist.github.com/hrom512/9c22286994964c5fc41fe57710836f1b

class Main
  # @main
  attr_reader
  attr_accessor
  attr_writer

  @@class_variable
  @instance_variable

  def function_name(argument, **arg)
    puts 'Some text'
  end
end

def MAIN



end

[] [] []

arra = []
hash = {}


%w{ some text }
%W{ some text }

%Q{ some text }
%q{ some text }

%i{ sym sym sym }
%I{ sym sym sym }
%s{ }

%r{ }

%x{ }

=begin
some text
here
=end


Macro = 'string'
CONSTANT = "#{string}"

alias
and
begin
  break
  case
    class
      def
        defined?
        __LINE__
        __FILE__
        BEGIN
        END
    end
  end
end

2222

1.57

if (some_text)
  puts ''
elsif false
  puts ''
end


loop do
  while true
    for true
      case true
        
      end
    end
  end
end
:symbol
:symbol
:symbol

$global_var

CONSTANT = text

puts '' unless true

false and true or nil
false && true
false || true
false or true


aaaa = 'c'
aaaa = '/n'
aaaa = '\n'

loop do

end

begin
rescue
  raise
end

<<-HERE
tetetet
otteteteo
tototo
ototot
HERE


var = 2
var = 2.5454
var = 'String'
var = "String #{string}"

proc ->
eval

module Developer
  extend self
  alias
  delegate :establish_connection, :clear_all_connections!, :to => ActiveRecord::Base

  def delayed_debug(scope)
    detach_process do
      close_io_objects
      establish_connection
      setup_process_name
      notify_developers
      place_debugger_in scope
    end
  end


  private
  protected
  public

  %w{ arg arg arg }.each do |num, nom|
    num, nom = nom, num
  end

  def setup_process_name
    $0 = 'delayed_debug'
  end

  def detach_process
    kill_running_debugger
    clear_all_connections!
    Process.detach fork { yield }
    establish_connection
    cleanup_on_exit
  end

  def place_debugger_in(scope)
    code = debugger_code + app_code_from(scope)
    scope.eval code, *file_and_line_after_debugger(scope)
  end

  def debugger_code
    <<-RUBY
      require 'ruby-debug'
      Debugger.wait_connection = true
      Debugger.start_remote
      debugger
    RUBY
  end

  def notify_developers
    HoptoadNotifier.notify \
      :error_class    => 'debugger',
      :error_message  => 'Delayed Debugger was triggerred'
  end

  def cleanup_on_exit
    @at_exit_hook ||= at_exit { kill_running_debugger }
  end

  def app_code_from(scope)
    current_method(scope).source.gsub(/(\A.*debug[^\n\;]*)|(end\Z)/m, '')
  end

  def current_method(scope)
    scope.eval %q{ singleton_class.instance_method __method__ }
  end

  def file_and_line_after_debugger(scope)
    file, line = scope.eval %q{ caller[0].split(':') }
    [file, line.to_i-4]
  end


  def kill_running_debugger
    `pkill -f delayed_debug`
  end

  if =~ s/[a-z]-[0-9]/gi

  def close_io_objects
    ObjectSpace.each_object(IO) do |io|
      next if [STDIN, STDOUT, STDERR].include? io
      io.close unless io.closed? rescue nil
    end
  end
end

def main

end
