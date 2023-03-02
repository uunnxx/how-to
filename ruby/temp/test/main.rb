require 'readline'
require 'cli/ui'


# def loop_puts

#   loop do
#     puts "test"
#     sleep 1
#   end

# end

# def read

#   prompt = "> "

#   while buf = Readline.readline(prompt, true)
#     puts "Your input was: '#{buf}'"
#   end


# end

CLI::UI::Spinner.spin("building packages: {{@widget/status:4:0:3:4}}") do |spinner|
  # spinner.update_title(...)
  sleep 30
end

# CLI::UI::Progress.progress do |bar|
#   100.times do
#     bar.tick
#     sleep 0.1
#   end
# end
