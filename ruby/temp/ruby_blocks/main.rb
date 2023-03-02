def my_method(&my_block)
  # when you call this method with a block, it will be stored in "my_block"
  puts "We're in the method, about to invoke your block!"
  # my_block parameter
  my_block.call # The "call" method calls the block.
  puts "We're back in the method!"
end

my_method do |x|
  puts "x: :#{x}: in the block"
end

def my_method2(&my_block)
  # ...
  my_block.call # Run the block's code
  # ...
end
