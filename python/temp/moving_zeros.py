def br(size=80, linebreak='-'):
    print()
    print(f'{linebreak * size}')
    print()


def move_zeros(lst):
    zero_count = 0
    result = []

    for _index, element in enumerate(lst):
        if element == 0:
            zero_count += 1
        else:
            result.append(element)
    if zero_count:
        result += zero_count * [0]

    return result

# Modified version with `list.count()` method
def move_zeros2(lst):
    result = []

    # count zeros
    zero_count = lst.count(0)
    # start iterate through if any
    if zero_count:
        for _index, element in enumerate(lst):
            if element != 0:
                # if element isn't 'zero' then append to the new list
                result.append(element)
        # we within if statement, so there ARE 'zero's, append them to the end of the list
        return result + zero_count * [0]
    # otherwise just return list itself
    return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 0, 9, 0, 0, 1, 0, 0, 0, 0, 0]))

br()

print(move_zeros2([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros2([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 0, 9, 0, 0, 1, 0, 0, 0, 0, 0]))


# Type annotations test
def main(name: str, age: int) -> int:
    name.upper()
    int(age)
    return age

main('Name', 22)



