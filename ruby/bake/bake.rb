# def add(x, y)
#   puts Integer(x) + Integer(y)
# end



# @parameter x [Integer] The x offset
# @parameter y [Integer] The y offset
def add(x: 10, y: 20)
  puts Integer(x) + Integer(y)
end

private
def puts(*arguments)
  $stdout.puts arguments.inspect
end
