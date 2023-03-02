# def winsize
#   require 'io/console'
#   puts IO.console.winsize
#   rescue LoadError
#   [Integer(`tput lines`), Integer(`tput cols`)]
# end


def lines
  current_shell_char_width = %x(tput cols).to_i
  current_shell_char_height = %x(tput lines).to_i

  # puts '#' * current_shell_char_height


  # puts current_shell_char_height
  # puts current_shell_char_width

  puts
  puts '#' * current_shell_char_width

  (current_shell_char_height-3).times do
    puts '##' << ' ' * (current_shell_char_width-4) << '##'
  end

  puts '#' * current_shell_char_width

end

lines
