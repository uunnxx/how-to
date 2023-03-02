def total(a = 5, *numbers, **phonebook):
    print('a', a)

    # Iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    # Iterate through all the items in dictionary
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

total(10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1560)

# How it works
# When we declare a starred parameter such as *param, then all the positional arguments from
# that point till the end are collected as a tuple called 'param'.

# Similarly, when we declare a double-starred parameter such as **param, then all the keyword
# arguments from that point till the end are collected as a dictionary called 'param'.
