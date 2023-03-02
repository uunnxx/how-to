# https://www.programming-idioms.org/idiom/253/print-stack-trace
# Print the stack frames of the current execution thread of the program.


def a
  b
end
def b
  puts caller
end

a


# stdin copy:
# Standard input is empty

# stdout copy:
# prog.rb:2:in `a'
# prog.rb:8:in `<main>'
