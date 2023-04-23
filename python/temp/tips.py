# any & all
x = [True, True, False]

if any(x):
    print('At least one True')
if all(x):
    print('Not one False')
if any(x) and not all(x):
    print('At least one True and one False')

# collections
# В Python есть отличные встроенные типы данных, но иногда
# они ведут себя не так, как вам бы хотелось.

# К счастью, в стандартной библиотеке Python присутствует модуль collections.
# Это полезное дополнение предлагает расширенные типы данных.

from collections import OrderedDict, Counter

# Remembers the order the keys are added!
x = OrderedDict(a=1, b=2, c=3)

# Counts the frequency of each character
y = Counter("Hello World!")

# inspect
# import inspect
# print(inspect.getsource(inspect.getsource))
# print(inspect.getmodule(inspect.getmodule))
# print(inspect.currentframe().f_lineno)

# Перезагрузка оператора
class Thing:
    def __init__(self, value):
        self.__value = value
    def __gt__(self, other):
        return self.__value > other.__value
    def __lt__(self, other):
        return self.__value < other.__value


something = Thing(100)
nothing = Thing(0)

# True
something > nothing

# False
something < nothing

# Error
# something + nothing

import requests
import pprint

# url = 'https://randomuser.me/api/?results=1'
# users = requests.get(url).json()

# pprint.pprint(users)


def add_two(x: int) -> int:
    return x + 2

from typing import List

Vector = List[float]
Matrix = List[Vector]


def add_matrix(a: Matrix, b: Matrix) -> Matrix:
    result = []
    for i, row in enumerate(a):
        result_row = [a[i][j] + b[i][j] for j, col in enumerate(row)]
        result += [result_row]
    return result

x = [[1.0, 0.0], [0.0, 1.0]]
y = [[2.0, 1.0], [0.0, -2.0]]

z = add_matrix(x, y)

print(z)


import uuid

user_id = uuid.uuid4()
print(user_id)


# Perform Boolean Masknig Without using numpy

from itertools import compress

# The compress will take an iterable and then selectors or boolean array.
# compress(data, selectors)


# Creating some list
my_list = [1, 4, 9, -2, 10, -7, 2, 3, -1, 6]

# Creating some booleans
# Returns true if a number is negative
my_bool = [i < 0 for i in my_list]
print(my_list)
print(my_bool)

# Our list comprehension returns True if the number is negative or False otherwise.


print()
print(list(zip(my_list, my_bool)))

# Now let's perform our boolean indexing:
# Filtering based on the booleans
# Geting values corresponding to the True boolean
print(list(compress(my_list, my_bool)))
# The data is compressed with our selectors and then the values in our data
# with corresponding True values are returned.

# As you can see the negative values in my_list were -2, -7, -1
# and they have all been returned.

from collections import Counter

# Creating some list
my_list = [
    2, 3, 4, 1, 2, 7, 3,
    4, 4, 5, 8, 4, 7, 8,
    2, 2, 7, 9, 0, 8, 4
]

# The Counter takes in an iterable, in this case my_list
# Creating a Counter object:
my_counter = Counter(my_list)

# Finding the two most common items in our list:
top_two = my_counter.most_common(2)
top_two


