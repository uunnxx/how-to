# good:
def the_answer = 42;
def get_x = @x;
def square(x) = x * x;

# Not (so) good: has side effect
def set_x(x) = (@x = x);
def print_foo = puts("foo");

# bad
def fib(x) = if x < 2
  x
else
  fib(x - 1) + fib(x - 2)
end


