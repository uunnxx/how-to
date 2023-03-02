def find(input_array)
  input_array.sort!
  sum_of_even = 0
  sum_of_odd = 0

  input_array.each_with_index do |element, index|
    if (index % 2).zero?
      sum_of_even += element
    else
      sum_of_odd += element
    end
  end
  sum_of_even - sum_of_odd
end

p find([1, 1, 2, 2, 3, 4, 4]) # => 3
p find([7, 1, 2, 2, 1, 4, 4]) # => 7
p find([1, 8, 3, 1, 3, 5, 5]) # => 8
p find([1, 6, 2, 5, 2, 6, 1]) # => 5
p find([1, 6, 2, 2, 1, 4, 4]) # => 6

puts
puts '-' * 80
puts

p [1, 1, 2, 2, 3, 4, 4].reduce(&:^) # => 3
p [7, 1, 2, 2, 1, 4, 4].reduce(&:^) # => 7
p [1, 8, 3, 1, 3, 5, 5].reduce(&:^) # => 8
p [1, 6, 2, 5, 2, 6, 1].reduce(&:^) # => 5
p [1, 6, 2, 2, 1, 4, 4].reduce(&:^) # => 6
