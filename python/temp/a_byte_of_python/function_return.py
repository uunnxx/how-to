# The `return` statement is used to return from a function i.e. break out of the function.
# We can optionally return a value from the function as well.

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))


def some_function():
    pass

# The `pass` statement is used in Python to indicate an empty block of statements.
# TIP: There is a built-in function called max that already implements the 'find maximum'
# functionality, so use this built-in function whenever possible.
