def br():
    print()
    print('-' * 80)
    print()

# Lists are one of these collection types, and they allow you to store
# indexed values:

x = ['hi', 'hello', 'welcome']
print(x[2])

br()

# Dictionaries are another collection type and allow you to map arbitrary keys
# to values.
# Dictionaries can be indexedin the same way as lists, using
# square brackets containing keys.

ages = {
    'Dave': 24,
    'Mary': 42,
    'John': 58
}

print(ages['Dave'])
print(ages['Mary'])


br()

# Only immutable objects can be used as keys to dictionaries. Immutable
# objects are those that can't be changed.
# So far, the only mutable objects you've come across are `lists` and `dictionaries`.

nums = {
    1: 'one',
    2: 'two',
    3: 'three'
}

print(1 in nums)
print('three' in nums)
print(4 not in nums)


br()

# A useful dictionary function is `get`. It does the same thing as indexed,
# but if the key is not found in the dictionary it returns another specified
# value instead.

pairs = {
    1: 'apple',
    'orange': [2, 3, 4],
    True: False,
    12: 'True'
}

print(pairs.get('orange'))
print(pairs.get(7, 42))
print(pairs.get(12345, 'not found'))

br()

# Tuples
# Tuples are very similar to lists, except that they are immutable
# (they cannot be changed).
# Also, they are created using `parentheses`, rather than square brackets.

# Example:
words = ('spam', 'eggs', 'sausages')
print(words[0])

w = (1)  # => int
x = ('string',)  # => tuple
print(type(w))
print(type(x))

br()

# list
lst = ['one', 'two']
dct = {1: 'one', 2: 'two'}
tupl = ('one', 'two')

# Tuples can be created without the parentheses by just separating the
# values with commas.

my_tuple = 'one', 'two', 'three'
print(my_tuple[0])
print(type(my_tuple))


# Tuples unpacking allows you to assign each item in a collection to a variable.

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

x, y = [1, 2]
x, y = y, x

br()

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

br()

# Sets are similar to lists or dictionaries.
# They are created using curly braces, and are unordered, which means that
# they can't be indexed.

# Due to the way they're stored, it's faster to check whether an item is part
# of a set using the `in` operator, rather than part of a list.

num_set = {1, 2, 3, 4, 5}
print(3 in num_set)

# You can use the `add()` function to add new items to the set, and `remove()`
# to delete a specific element:

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)

nums.add(-7)
nums.remove(3)
print(nums)
print(f'Len: {len(nums)}')

# Duplicate elements will automatically get removed from the set.
# The `len()` function can be used to return the number of elements of a set.

br()

# Sets can be combined using mathematical operations.
# The `union` operator `|` combines two sets to form a new one containing items in either.
# The `intersection` operator `&` gets items only in both.
# The `difference` operator `-` gets items in the first set but not in the second
# The `symmetcric difference` operator `^` gets items in either set, but not both.

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(second ^ first)


br()

# List comprehensions are a useful way of quickly creating lists whose
# contents obey a rule.
# For example, we can do the following:

# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

br()

# A list comprehension can also contain an `if` statement to enforce
# a condition on values in the list.
evens = [i**2 for i in range(10) if i % 2 == 0]
print(evens)

br()

# word = input()
word = 'awesome'
vowels = ['a', 'e', 'i', 'o', 'u']
output_list = [i for i in word if i not in vowels]
print(output_list)


# Data Structures
# As we have seen in the previous lessons, Python supports the following
# collection types: Lists, Dictionaries, Tuples, Sets.

# When to use a dictionary:
# - when you need a logical association between a key:value pair.
# - when you need fast lookup for your data, based on a custom key.
# - when your data is being constantly modified.
#     Remember, dictionaries are MUTABLE.

# When to use the other types:
# - Use LISTS if you have a collection of data that does not need random access.
#   Try to choose lists when you need a simple, iterable collection that is
#   modified frequently.
# - Use SET if you need uniqueness for the elements.
# - Use TUPLES when your data cannot/should not change.

# Many times, a TUPLE is used in combination with a dictionary, for
# example, a TUPLE might represent a key, because it's immutable.



br()


# Functional Programming
# Functional programming is a style of programming that (as the name suggest)
# is based around functions.

# A key part of functional programming is `higher-order functions`.
# Higher-order functions take other functions as arguments, or return
# them as results.

# Examlple:
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))


def test(func, arg):
    return func(func(arg))

def mult(x):
    return x * x

print(test(mult, 2))


# Pure Functions
# Functional programming seeks to use pure functions. Pure functions have
# no side effects, and return a value that depends ONLY on their arguments.
# This is how functions in math work: for example, the `cos(x)` will, for
# the same value of `x`, always return the same result.

# Below are examples of pure and impure functions:

# Pure function:
def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)

# Impure function:
some_list = []
def impure(arg):
    some_list.append(arg)

# The function above is not pure, because it changed the state of `some_list`.

# Using pure functions has both advantages and disadvantages.
# Pure functions are:
# - easier to reason about and test.
# - more efficient. Once the function has been evaluated for an input,
#   the result can be stored and referred to the next time the function of
#   that input is needed, reducing the number of times the function is called.
#   This is called `memoization`.
# - easier to run in parallel.

# Pure functions are more difficult to write in some situations.

br()

# Lambdas
# Creating a function normally (using `def`) assigns it to a variable
# with its name automatically.
# Pytohn allows us to create functions on-the-fly, provided that they are
# created using `lambda` syntax.

# This approach is most commonly used when passing a simple function
# as an argument to another function. The syntax is shown in the next
# example and consists of the `lambda` keyword followed bby a list of
# arguments, a colon, and the expression to evaluate and return.


def my_func(f, arg):
    return f(arg)

print(my_func(lambda x: 2*x*x, 5))


# Lambda functions aren't as powerful as named functions.
# They can only do things that require a single expression -- usually
# equivalent to a single line of code.

# named function
def polynominal(x):
    return x**2 + 5*x + 4

print(polynominal(-4))


# lambda
print((lambda x: x**2 + 5*x + 4)(-4))

# You are given code that should calculate the corresponding percentage of a price.
# Somebody wrote a lambda function to accomplish that, however the lambda is wrong.
# Fix the code to output the given percentage of the price.
#
# Sample Input
# 50
# 10
#
# Sample Output
# 5.0

# price = int(input())
# perc = int(input())
#
# res = (lambda price, perc: price * (perc / 100))(price, perc)


br()

# map
# The built-in functions `map` and `filter` are very useful higher-order
# functions that operate on lists (or similar objects called `iterables`).

# The function `map` takes a function and an iterable as arguments, and
# returns a new iterable with the function applied to each argument.

# Example:
# def add_five(x):
#     return x + 5
#
# nums_list = [11, 22, 33, 44, 55]
# result = list(map(add_five, nums_list))
# print(result)

# We could have achieved the same result more easily by using
# `lambda` syntax.

br()
# nums_list = [11, 22, 33, 44, 55]
# result = list(map(lambda x: x+5, nums_list))
# print(result)
br()


# map
# Fill in the blanks to multiply each item in the list by 2 using lambda syntax.

# nums_list = [11, 22, 33]
# a = list(map(lambda x: x*2, nums_list))


# filter
# The function `filter` filters an iterable by leaving only the items
# that match aa condition (also called a `predicate`).

# Example:
# nums_list = [11, 22, 33, 44, 55]
# res = list(filter(lambda x: x % 2 == 0, nums_list))
# print(res)

# Like `map`, the result has to be explicitly converted to a list if you
# want to print it.

# nums_list = [1, 2, 5, 8, 3, 0, 7]
#
# res = list(filter(lambda x: x < 5, nums_list))
#
# print(res)

br()

# Generators
# `Generators` are a type of iterable, like lists or tuples.
# Unlike lists, they don't allow indexing with arbitrary indices, but they
# can still be iterated through with `for` loops.

# Example:
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


# Generators
# Due to the fact that they `yield` one item at a time, `generators`
# don't have the memory restrictions of lists.
# In fact, they can be `infinite!`

def infinite_sevens():
    while True:
        yield 7


# for i in infinite_sevens():
#     print(i)

# In short, `generators` allow you to declare a function that behaves
# like an iterator, i.e. it can be used in a `for` loop.


# Finite generators can be converted into lists by passing them as
# arguments to the `list` function.

def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(numbers(11)))

# Using `generators` results in improved performance, which is the result
# of the lazy (on demand) generation of values, which translates to lower
# memory usage. Furthemore, we do not need to wait until all the elements
# have been generated before we start to use them.


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True

    for n in range(2, x):
        if x % 2 == 0:
            return False
    return True


def prime_generator(a, b):
    for i in range(a, b):
        if is_prime(i):
            yield i


# f = int(input())
# t = int(input())
f = 5
t = 10

print(list(prime_generator(f, t)))

br()


# Decorators
# Decorators provide a way to modify functions using other functions.
# This is ideal when you need to extend the functionality of functions that
# you don't want to modify.

# Example:

def decor(func):
    def wrap():
        print('-' * 40)
        func()
        print('-' * 40)
    return wrap

def print_text():
    print('Hello world!')

decorated = decor(print_text)
decorated()


# In our previous example, we decorated our function by replacing the
# variable containing the function with a wrapped version.

# def print_text():
#     print('Hello world!')
#
# print_text = decor(print_text)
#

# This pattern can be used at any time, to wrap any function.
# Python provides support to wrap a function in a decorator by pre-pending
# the function definition with a decorator name and the @ symbol.
# If we are defining a function we can 'decorate' it with the @ symbol like:

# @decor
# def print_text():
#     print('Hello world!')

# This will have the same result as the above code.

###############################################

def pr(func):
    def wrapper(*args, **kwargs):
        print('-' * 80)
        func(*args, **kwargs)
        print('-' * 80)

    return wrapper


def ppp(args):
    print(args)


p = pr(ppp)
# p('some text')


p(type(str))


br()


def decor2(func):
    def wrapper(*args):
        print('***')
        func(*args)
        print('***')
        print('END OF PAGE')

    return wrapper


@decor2
def invoice(num):
    print(f"INVOICE #{num}")


invoice(42)

br()



# Recursion
# Recursion is a very important concept in functional programming.
# The fundamental part of recursion is self-reference -- function calling
# themselves. It is used to solve problems that can be broken up into
# easier sub-problems of the same type.

# A classic example of a function that is implemented recursively is the
# `factorial` function, which finds the product of all positive integers below
# a specified number.
# For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (=120). To implement
# this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and
# so on. Generally, n! = n * !(n-1).
# Furthemore, 1! = 1. This is known as the `base case`, as it can be
# calculated without performing any more factorials.
# Below is a recursive implementation of the factorial function.

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

# The `base case` acts as the exit condition of the recursion.
# Not adding a base case results in infinite function calls, crashing the
# program.

# Recursion can also be indirect. One function can call a second, which
# calls the first, which calls the second, and so on. This can occur with
# any number of functions.

# Example:

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))



# Decimal to Binary
def convert(num):
    if num < 2:
        return 1
    return (num % 2 + 10 * convert(num // 2))


print(convert(42))
