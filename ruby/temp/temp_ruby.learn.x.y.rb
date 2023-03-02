# learn x in y minutes
# where x=ruby


=begin
some comments here
multiline
=end

# In Ruby, (almost) everything is an object.
# This includes numbers...
3.class # => Integer

# ...and strings...
'Hello'.class # =>  String

# ...and even methods!
'Hello'.method(:class).class # => Method

# Some basic arithmetic
1 + 1 # => 2
8 - 1 # => 7
10 * 2 # => 20
35 / 5 # => 7
2 ** 5 # => 32
5 % 3 # => 2

# Bitwise operators
3 & 5 # => 1
3 | 5 # => 7
3 ^ 5 # => 6

# Arithmetic is just syntactic sugar
# for calling a method on an object
1.+(3) # => 4
10.* 5 # => 50
100.methods.includes(:/) # => true

# Special values are objects
nil # => equivalent to null in other languages
true # => trutch
false # => falsehood

nil.class # => NilClass
true.class # => TrueClass
false.class # => FalseClass

# Equality
1 == 1 # => true
2 == 1 # => false

# Inequality
1 != 1 # => false
2 != 1 # => true

# Apart from false itself, nil is the only other 'falsey' value


!!nil # => false
!!false # => false
!!0 # => true
!!"" # => true

# More comparisions
1 < 10 # => true
1 > 10 # => false
2 <= 2 # => true
2 >= 2 # => true


