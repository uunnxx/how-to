# Ruby Descending Order Method
#
# Method takes a non-negative integer (n) as an argument then:
# - turns it into a string
# - splits each character in the string into an array of strings
# - sorts the array alphabetically
# - joins the strings together in ascending order
# - reverses the string and turns it back into an integer
#
# Let me know if you found a better way!

def descending_order(n)
  n.to_s.split("").sort_by {|x| x}.join("").reverse.to_i
end

# alternative version:
def descending_order(n)
  n.digits.sort_by { |c| -c.ord }.join.to_i
end

# This does a few interesting things:

# - It uses the Integer#digits method, which is effectively the same as int.to_s.chars or int.to_s.split('')
# - It uses the ord method to get the numeric representation of a character, but negates it to get back to an ascending order, much the same as one would do with a numeric list
# - join doesn't require '' as it'll assume that.
#
# Granted there are likely better ways to go about it, but this gives some interesting ideas.

# source:
# https://dev.to/chair/ruby-descending-order-method-4nac
