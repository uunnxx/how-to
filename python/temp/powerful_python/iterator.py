def br():
    print()
    print('-----------------------------------------------------------')
    print('-----------------------------------------------------------')
    print('-----------------------------------------------------------')
    print()

# class BrokenInLoops:
#     def __init__(self):
#         self.items = [7, 3, 9]
#     def __iter__(self):
#         return self.items
#
# items = BrokenInLoops()
# for item in items:
#     print(item)
#


class BrokenInLoops:
    def __init__(self):
        self.items = [7, 3, 9]
    def __iter__(self):
        return iter(self.items)

items = BrokenInLoops()
for item in items:
    print(item)


br()


class WorksInLoops():
    """docstring for WorksInLoops"""
    def __init__(self):
        self.items = [7, 3, 9]
    def __iter__(self):
        # This class is identical to BrokenInLoops,
        # except for this next line.
        return iter(self.items)

items = WorksInLoops()
for item in items:
    print(item)

br()

squares = [ n*n for n in range(6) ]
print(squares)

br()

squares2 = [n*n for n in range(6)]
print(squares2)

br()

blocks = { n: 'x' * n for n in range(6) }
print(blocks)

br()

blocks2 = {n: 'x' * n for n in range(6)}
print(blocks2)

br()

# First define some source sequences...
pets = ['dog', 'parakeet', 'cat', 'llama']
numbers = [9, -1, -4, 20, 11, -3]

def repeat(s):
    return s + s

print([ 2 * m + 3 for m in range(10, 20, 2) ])
print([ abs(num) for num in numbers ])
print([ 10 - x for x in numbers ])
print([ pet.lower() for pet in pets ])
print([f'The {pet}' for pet in sorted(pets)])
print([ repeat(pet) for pet in pets ])

br()

print(type(squares))

br()

def is_palindrome(word):
    return word == word[::-1]

words = ['bib', 'bias', 'dad', 'eye', 'deed', 'tooth']

print([ n * 2 for n in numbers if n % 2 == 0 ])
print([ pet.upper() for pet in pets if len(pet) == 3 ])
print([ n for n in numbers if n > 0 ])
print([ n for n in numbers if n > 0 ])
print([ word for word in words if is_palindrome(word) ])

br()

# Formatting for readability (and more)

def double_short_words(words):
    return [ word + word
            for word in words
            if len(word) < 5 ]

def double_short_words2(words):
    return [
            word + word
            for word in words
            if len(word) < 5
            ]

colors = [ 'orange', 'puprle', 'pink' ]
toys = [ 'bike', 'basketball', 'skateboard', 'doll' ]

print([f'{color} {toy}' for color in colors for toy in toys])

br()

ranges = [ range(1, 7), range(4, 12, 3), range(-5, 9, 4) ]
print([ float(num)
        for subrange in ranges
        for num in subrange ])


br()

build_colors_toys = []
for color in colors:
    build_colors_toys.extend(f'{color} {toy}' for toy in toys)
print(build_colors_toys[0])

br()

def pp(func):
    def wrapper():
        print('--------')
        func()
        print('--------')
    return wrapper


@pp
def say_hi():
    print('hi')

say_hi()

br()


def log_return(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        print(res)
        return res
    return wrapper


@log_return
def f(*args, **kwargs):
    return args, kwargs

f(1, 2, 3, a=4, b=5)
f((1, 2, 3), {'a': 4, 'b': 5})
f((1, 2, 3), {'a': 4, 'b': 5})
