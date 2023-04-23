def br():
    print()
    print('-' * 80)
    print()


my_items = ['a', 'b', 'c']

for my_item_ in my_items:
    print(my_item_)
br()

print(range(len(my_items)))

br()

print(list(range(3)))

br()

for my_item in my_items:
    print(my_item)

br()

for item in my_items:
    print(item)

br()


for i, item in enumerate(my_items):
    print(f'{i}: {item}')

br()


emails = {
        'Bob': 'bob@example.com',
        'Alice': 'alice@example.com'
        }

for name, email in emails.items():
    print(f"{name} -> {email}")

br()

"""
values = [expression for item in collection]

values = []
for item in collection:
    values.append(expression)
"""

squares = [x * x for x in range(10)]

# or
"""
squares = []
for x in range(10):
    squares.append(x * x)



"""

print(squares)


br()

even_squares = [x * x for x in range(10) if x % 2 == 0]

# even_squares = [x * x for x in range(10)
#         if x % 2 == 0]

print(even_squares)

"""
even_squares = [] for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)
"""

"""
values = [expression
        for item in collection
        if condition]


values = [] for item in collection:
    if condition:
        values.append(expression)
"""

br()

{x * x for x in range(-9, 10)}
{x: x * x for x in range(-9, 10)}

lst = [1, 2, 3, 4, 5]

# lst[start:stop:step]

print(lst)
print(lst[1:3])
print(lst[1:3:1])


br()


class Repeater:
    """description"""
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        return RepeaterIterator(self)


class RepeaterIterator:
    """docstring for RepeaterIterator"""
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value


repeater = Repeater('Hi')
for item in repeater:
    print(item)
