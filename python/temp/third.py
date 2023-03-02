# 4.3 COMPLEX DATA TYPES
# List:
l = [1, 2, 3, 4]
print(len(l)) # => 3

# Adding elements to a list with append, insert, or list concatenation.
# The append operation is fastest.
l.append(5) # => [1, 2, 3, 4, 5]
l.insert(2, 2) # => [1, 2, 2, 4, 5]
l + [6] # => [1, 2, 3, 4, 5, 6]

# Removing elements is slower (find it first).
l.remove(1)

# Reversing the order of elements.
l.reverse()

# Sorting a list.
# Slow for large lists: O(n log n), n list elements.
l.sort()

# Indexing
# Finds index of the first occurence of an element in the list.
# Is slow when traversing the whole list.
[2, 2, 4].index(2) # index of element 4 is 0
[2, 2, 4].index(2, 1) # index of element 2 after pos 1 is "1"

# Stack
# Python lists can be used intuitively as stack via the two list operations append() and pop()
stack = [3]
stack.append(42) # [3, 42]
stack.pop() # 42 (stack: [3])
stack.pop() # 3 (stack: [])

# Set
# Unordered collection of unique elements (at-most-once).
basket = {'apple', 'eggs', 'banana', 'orange'}
same = set(['apple', 'eggs', 'banana', 'orange'])
print(basket == same) # True

# Dictionary
# A useful data structure for storing (key, value) pairs.
calories = {'apple': 52, 'banana': 89, 'choco': 546}

# Reading and writing
# Read and write elements by specifying the key within the brackets.
# Use the keys() and values() functions to access all keys and values of the dictionary.
c = calories
print(c['apple'] < c['choco']) # True
c['cappu'] = 74
print(c['banana'] < c['cappu']) # False
print('apple' in c.keys()) # True
print(52 in c.values()) # True

# Dictionary Looping
# You can access the (key, value) pairs of a dictionary with the items() method.
for k, v in calories.items():
    print(k) if v > 500 else None # 'chocolate'

# Membership operator
# Check with the keyword 'in' whether the set, list, or dictionary contains an element.
# Set containment is faster than list containment.
basket = {'apple', 'eggs', 'banana', 'orange'}
print('eggs' in basket) # True
print('mushroom' in basket) # False

# List and Set Comprehension
# List comprehension is the concise Python way to create lists. Use brackets plus an expression,
# followed by a for clause. Close with zero or more for or if clauses.
## List comprehension
[('Hi ' + x) for x in ['Alice', 'Bob', 'Pete']]
# ['Hi Alice', 'Hi Bob', 'Hi Pete']
[x * y for x in range(3) for y in range(3) if x > y] # [0, 0, 2]

# Set comprehension is similar to list comprehension.
## Set comprehension
squares = { x**2 for x in [0,2,4] if x < 4 } # {0, 4}
