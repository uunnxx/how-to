from random import randint
import timeit


# list [4, 3, 2, 1]desc --> [1, 2, 3, 4]asc

# [4, 3, 2, 1] --> [3, 4, 2, 1] --> [3, 2, 4, 1] --> [3, 2, 1, 4]
# [3, 2, 1, 4] --> [2, 3, 1, 4] --> [2, 1, 3, 4]
# [2, 1, 3, 4] --> [1, 2, 3, 4] --> sorted


def bubble_sort(lst: list) -> list:
    lst_len = len(lst)

    for i in range(lst_len):
        for j in range(lst_len - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def run_sorting(algorithm, lst: list) -> None:
    setup_code = f'from __main__ import {algorithm}'
    stmt = f'{algorithm}({lst})'
    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)

    print(f'Quickest execution time: {min(time)}')




if __name__ == '__main__':
    # lst: list = [2, 32, 1, 67, 27, 21, 100, 150]
    lst: list = [randint(0, 100) for _ in range(1000)]
    # print(sorted(lst))
    # print(sorted(lst, reverse=True))
    # print(bubble_sort(lst))
    run_sorting(algorithm='bubble_sort', lst=lst)
