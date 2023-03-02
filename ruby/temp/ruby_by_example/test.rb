def first_if_true(first, second, to_be_tested)
  if to_be_tested
    puts first
  else
    puts second
  end
end

first_if_true 1, 2, true


pp 'break at each space'.split(' ')


=begin rdoc
Parses command line options
=end
class SimpleCLI
  OPTIONS = {
    version: ['-v', '--version'],
    help: ['-h', '--help'],
    reset: ['-r', '--reset']
  }

  USAGE =<<-END_OF_USAGE
  This program understands the following options:
  -v, --version : displays the current version of the program
  -h, --help    : displays a message with usage instructions
  -r, --reset   : resets the program

  With no command-line option, the program perform its default behavior.

  END_OF_USAGE

  VERSION = 'Some Project version 0.0.1 (Pre-Alpha)\n'

  def parse_opts args
    return option_by_args(args[0]) if understand_args?(args)
    display(USAGE)
  end

  private

end
