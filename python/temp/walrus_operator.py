# The Walrus operator (:=) was introduced in Python 3.8, it can be useful in situations where you'd want to assign values to variables within an expression.

def some_func():
        # Assume some expensive computation here
        # time.sleep(1000)
        return 5

# So instead of,
if some_func():
        print(some_func()) # Which is bad practice since computation is happening twice

# or
a = some_func()
if a:
    print(a)

# Now you can concisely write
if a := some_func():
        print(a)

# Output (> 3.8):
# 5
# 5
# 5
