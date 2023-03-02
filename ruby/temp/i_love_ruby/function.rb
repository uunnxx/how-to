def linebreak
  puts ''
  puts '-' * 100
  puts ''
end



def print_line
  puts "_" * 20
end

print_line
puts "This program prints lines"
print_line

linebreak

def print_line2 length
  puts "_" * length
end

10.step(50, 10) do |x|
  print_line2 x
end

40.step(10, -10) do |x|
  print_line2 x
end

linebreak

# Default Argument
def print_line3 length = 20
  puts "_" * length
end

print_line3

linebreak

# 9.3 Passing array to a function
def array_changer array
  array << 6
end

some_array = [1, 2, 3, 4, 5]
p some_array
array_changer some_array
p some_array

=begin
  Output:
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5, 6]

    If you are newcomer to programming, this might not be surprising, but when a variable is passed to
    a function, its value is not supposed to change. But in case of array, inside the function
    `array_changer`, we rae adding an element to it and it changes. Well this is a peculiar behavior
    of an array getting passed to a function.

    To avoid such behaviour try the program below
=end

linebreak

def array_changer2 array
  array << 6
end

some_array = [1, 2, 3, 4, 5]
p some_array
array_changer2 Marshal.load(Marshal.dump(some_array))

=begin
  Output:
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
=end

linebreak

# 9.4 Returning Values

def addition x, y
  x + y
end

a, b = 3, 5
p addition a, b

linebreak
def square_it x
  x**2
end

p square_it 5


linebreak

# 9.5 Keyword arguments

def say_hello name: 'Martin', age: 33
  puts "Hello #{name} your age is #{age}"
end

say_hello name: 'Joseph', age: 7
say_hello age: 21, name: 'Vignesh'
say_hello

puts ''

def factorial num
  fact = 1
  1.upto(num) do |a|
    fact = fact * a
  end
  fact
end

number = 17
puts "Factorial of #{number} = #{factorial number}"

def factorial2 num
  return 1 if num == 1

  num * factorial2(num - 1)
end

number2 = 15
puts "Factorial of #{number2} = #{factorial2 number2}"

linebreak

# 9.8 Hashes as function arguments
def some_function first_arg, others_as_hash
  puts "Your first argument is: #{first_arg}"
  puts "Other arrguments are:"
  others_as_hash.each do |x|
    p x
  end
end

some_function 'Yoda', {jedi: 100, sword: 100, seeing_future: 100}

# linebreak

# Chapter 10. Varibale Scope

# x = 5
#
# def print_x
#   puts x
# end

# print_x

linebreak

# Chapter 11. Classes & Objects
# 11.1 Creating a Square

class Square
  attr_accessor :side_length
end

s1 = Square.new
s1.side_length = 5
puts "Side length of s1 = #{s1.side_length}"

linebreak

