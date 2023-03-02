text = 'BLOCKT'
def line(width: 100, sym: '=', text: '')
  if text
    length = text.length+4
    # half = (width - length) / 2

    puts sym

    # puts sym * width
    # puts sym * half << '  ' << text.upcase << '  ' << sym * half
    # puts sym * width
  else
    puts
    puts "=" * width
    puts
  end
end

line(sym: '#', text: '')

# def hello
#   puts 'Hello, world!'
# end

# send(:hello)

# class Name
#   def family_name=(family)
#     @family_name = family
#   end

#   def given_name=(given)
#     @given_name = given
#   end
# end

# n = Name.new

# n.family_name = 'Matsumoto'
# n.given_name = 'Yukihiro'
# p n

# def repeat(word = 'Hello! ', times = 3)
#   puts word * times
# end

# def repeat(word: 'Hello! ', times: 3)
#   puts word * times
# end

# repeat

# line

# repeat(times: 5, word: 'Goodbye! ')

# line

# def num_args( *args )
#   length = args.size
#   label = length == 1 ? " argument" : " arguments"
#   num = length.to_s + label + " ( " + args.inspect + " )"
#   num
# end

# puts num_args
# puts num_args(1)
# puts num_args(100, 2.5, "Three")

# line

# def two_plus(one, two, *args)
#   length = args.size
#   label = length == 1 ? ' variable argument' : ' variable arguments'
#   num = length.to_s + label + ' ( ' + args.inspect + ' )'
#   num
# end

# puts two_plus(1, 2) # => 0 variable arguments ([])
# puts two_plus(1000, 3.5, 14.3) # => 1 variable arguments([14.3])
# puts two_plus(100, 2.5, 'three', 70, 14.3) # => 3 variable arguments (['three', 70, 14.3])

# line


# def greet
#   'Hi'
# end

# alias hi greet # => alias greet as hi
# puts hi

# line

# class Greeting
#   def greet
#     "Hi >>> #{self}"
#   end
#   alias_method :hi, :greet
# end

# puts Greeting.new.hi



# line

