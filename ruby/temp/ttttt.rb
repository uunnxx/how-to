args = ''
ARGV.each do |arg|
  args << "-e #{arg} "
end

puts args
