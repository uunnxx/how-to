import itertools
import operator
import functools


def br(sym='-', width=80):
    print(f"\n{sym * width}\n")


def flatten_list(_list):
    flat_list = []
    for element in _list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
print(f"Original list {nested_list}")
print(f"Flattened list {flatten_list(nested_list)}")

br()

# List comprehension
regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]
flat_list = [item for sublist in regular_list for item in sublist]

print(f"Original list {regular_list}")
print(f"Flattened list {flat_list}")

br()

# Recursive version


def flatten(list_of_lists):
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


# Standard libraries


regular_list = []


def transform(nested_list):
    for el in nested_list:
        if type(el) is list:
            regular_list.append(el)
        else:
            regular_list.append([el])
    return regular_list


irregular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9], [10, 11], [12]]
regular_2D_list = transform(irregular_list)
print(f"Original list {irregular_list}")
print(
    f"Flattened list {functools.reduce(operator.iconcat, regular_2D_list, [])}"
)

br()


flat_list = list(itertools.chain(*regular_list))

print(f"Original list {regular_list}")
print(f"Flattened list {flat_list}")

br()

regular_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9]]

flat_list = sum(regular_list, [])

print('Original list', regular_list)
print('Transformed list', flat_list)

br()

irregular_list = [[1, 2, 3], [3, 6, 7], [7, 5, 4], 7]

# Using lambda arguments: expression

irregular_list = [[1, 2, 3], [3, 6, 7], [7, 5, 4], 7]

# Using lambda arguments: expression
flatten_list = lambda irregular_list: [element for item in irregular_list for element in flatten_list(item)] if type(irregular_list) is list else [irregular_list]

print("Original list ", irregular_list)
print("Transformed List ", flatten_list(irregular_list))
