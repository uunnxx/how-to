import timeit
from random import randint


nts = [4, 3, 2, 1]


def insertion_sort(numbers: list[int]) -> list[int]:
    for i in range(1, len(numbers)):
        current_num = numbers[i]
        position = i - 1

        while position >= 0 and numbers[position] > current_num:
            numbers[position + 1] = numbers[position]
            position -= 1

        numbers[position + 1] = current_num



def run_sorting(algorithm, numbers):
    setup_code = f'from __main__ import {algorithm}'
    stmt = f'{algorithm}({numbers})'

    time = timeit.repeat(stmt=stmt, setup=setup_code, repeat=1, number=1)

    print(f'Quickest execution time: {min(time)}')



if __name__ == '__main__':
    nts = [randint(0, 10_000) for i  in range(5000)]
    run_sorting(algorithm='insertion_sort', numbers=nts)
