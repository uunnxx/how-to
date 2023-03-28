def br():
    print(f"\n{'-' * 80}\n")


def power_two_gen(max_num=0):
    """Program to print the Power of two up to the given number"""
    n = 1
    while n < max_num:
        yield 2 ** n
        n += 1


a = power_two_gen(6)

for i in a:
    print(i)


br()


# A simple generator for Fibonacci Numbers
def fib(max_num):
    # Initialize first two Fibonacci Numbers
    p, q = 0, 1

    # yield next Fibonacci Number one at a time
    while p < max_num:
        yield p
        p, q = q, p + q


# Ask the user to enter the maximum number
# fib_num = int(input("Enter the number: \n"))
fib_num = 4

# Create a generator object
x = fib(fib_num)
# Iterating over the generator object using for
# in a loop.
print(f"Resultant Series up to {fib_num} is :")
for i in x:
    print(i)


br()
