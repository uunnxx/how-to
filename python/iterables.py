# Introduction to Iterators and Generators


## Iteration


# - As you know, Python has a 'for' statement
# - You use it to iterate over a collection of items
for x in [1, 4, 5, 10]:
    print(x, end=' ')
print()

# - And, as you have probably noticed, you can iterate over many different kinds of objects (not just lists)


## Iterating over a Dict


# - If you iterate over a dictionary you get keys
prices = {
    'GOOG': 490.12,
    'AAPL': 752.34,
    'YHOO': 12.11
}

for key in prices:
    print(key)


## Iterating over a String


# - If you iterate over a string, you get characters
s = 'Yow!'
for char in s:
    print(char)


## Iterating over a File


# - If you iterate over a file you get lines
# for line in open('real.txt'):
#     print(line, end='')

### Consuming Iterables
# - Many operations consume an 'iterable' object
# - Reductions:
# sum(s), min(s), max(s)

# - Constructors
# list(s), tuple(s), set(s), dict(s)

# - Various operators
# item in s

# - Many others in the library


## Iteration Protocol


# - The reason why you can iterate over different objects is that there is a specific protocol
# items = [1, 4, 5]
# it = iter(items)
# print(it.__next__())
# print(it.__next__())
# print(it.__next__())
# print(it.__next__()) # -> StopIteration Error

# - An inside look at the for statement
# for x in obj:
#     statements

# - Underneath the covers
# _iter = iter(obj)             # Get iterator object
# while l:
#     try:
#         x = _iter.__next__()  # Get next item
#     except StopIteration:     # No more items
#         break
#     ...

# - Any object that supports iter() is said to be 'iterable'


## Supporting Iteration


# - User-defined objects can support iteration
# - Example: Countdown down...
# for x in countdown(10):
#     print(x, end=' ')
#
# 10 9 8 7 6 5 4 3 2 1

# - To do this, you have to make the object implement __iter__() and __next__()
# - Sample implementation

class countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return countdown_iter(self.start)


class countdown_iter:
    def __init__(self, count):
        self.count = count

    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1

        return r


## Iteration Commentary


# - There are many subtle details involving the design of iterators for various objects
# - However, we're not going to cover that
# - This isn't a tutorial on 'iterators'
# - We're talking about generators...


## Generators


# - A generator is a function that produces a sequence of results instead fo a single value

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i, end=' ')



