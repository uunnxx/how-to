from typing import Any


mylist: list[Any] = [[1, 2, [3, [4, [5, (5.5, [5.8])]]]], 6, 7, 8]


def flatten(lst: list, result: list = []) -> list[Any]:
    for e in lst:
        if isinstance(e, list | tuple):
            flatten(e, result)
        else:
            result.append(e)

    return result


print(flatten(mylist))
