def yieldExample
  puts ">> Here , you are inside the method"
  yield
  puts ">> Again you fall under method block"
  yield
end

yieldExample do
  puts "---- This is the block of the code ----"
end



def yieldExample2
  yield 5
  puts ">> You are inside the method yieldExample"
  yield 100
end

yieldExample2 do |i|
  puts "---- This is the iteration number  #{i} ----"
end


def yieldExample3
  yield "Ranjan Kumar Pandey"
  puts ">> Inside the method yieldExample"
  yield "Ajay Sharma"
end

yieldExample3 do |name|
  puts "---- Your name is #{name} ----"
end

puts "\n\n\n\n\n\n\n\n"



def arithmetic(a, b)
  yield(a, b)
end

puts "The sum of the two numbers is #{arithmetic(8, 2) { |a, b| a + b }}" # addition of two number
puts "The multiplication of the two numbers is #{arithmetic(8, 2) { |a, b| a * b }}" # multiplication of two numbers
puts "The subtraction of the two numbers is #{arithmetic(8, 2) { |a, b| a - b }}" # subtraction of two numbers
puts "The division of the two numbers is #{arithmetic(8, 2) { |a, b| a / b }}" # division of two numbers
