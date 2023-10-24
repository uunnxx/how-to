lst: list = ['a', 'b', [[1, 2], [3, 4], [5, 6]], ['one', 'two'], ['three', 'four'], ['five', 'six'], (1, 2)]

# print(lst)


def flatten(lst: list, result=[]) -> list:
    for item in lst:
        if isinstance(item, int | str | float):
            result.append(item)
        else:
            flatten(item, result)

    return result


print(flatten(lst))
