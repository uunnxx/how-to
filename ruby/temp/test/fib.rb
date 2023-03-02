def fib(n)
  new, old = 1, 0
  n.times { new, old = new + old, new }
  old
end

# times = ARGV[0].to_i
tms = 100

tms.times.each do |i|
  puts fib(i)
end

puts "Hi"
