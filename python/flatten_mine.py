from typing import Any


lst: list[Any] = ['a', 'b', [[1, 2], [3, 4], [5, 6]], ['one', 'two'], ['three', 'four'], ['five', 'six'], (1, 2)]

def flatten(lst: list, result=[]) -> list[Any]:
    for item in lst:
        if isinstance(item, int | str | float):
            result.append(item)
        else:
            flatten(item, result)

    return result


print(flatten(lst))
