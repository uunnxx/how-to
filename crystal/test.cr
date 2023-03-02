# if rand(2) > 0
#   my_string = "hello world"
# end

# puts my_string.upcase

def shout(x)
  # Notice that both Int32 and String respond_to `to_s`
  x.to_s.upcase
end

foo = ENV["FOO"]? || 10

puts typeof(foo) # => (Int32 | String)
puts typeof(shout(foo)) # => String
