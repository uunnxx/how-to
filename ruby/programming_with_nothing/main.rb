puts lambda { |x| x + 1 }.call(41)
puts lambda { |x| x + 1 }[42]

puts '-----------------------------------------------------------------------'


lambda do |x|
  lambda do |y|
    puts x + y
  end
end[3][4]


# (1..100).each do |n|
#   if (n % 15).zero?
#     puts 'FizzBuzz'
#   elsif (n % 3).zero?
#     puts 'Fizz'
#   elsif (n % 5).zero?
#     puts 'Buzz'
#   else
#     puts n.to_s
#   end
# end


# (1..100).map do |n|
#   if (n % 15).zero?
#     'FizzBuzz'
#   elsif (n % 3).zero?
#     'Fizz'
#   elsif (n % 5).zero?
#     'Buzz'
#   else
#     n.to_s
#   end
# end


1.upto 100 do |i|
  puts i % 15 == 0 ? 'FizzBuzz' : i % 3 == 0 ? 'Fizz' : i % 5 == 0 ? 'Buzz' : i
end


(1..100).each do |i|
  puts i % 15 == 0 ? 'Fizzbuzz' : i % 3 == 0 ? 'Fizz' : i % 5 == 0 ? 'Buzz' : i
end
