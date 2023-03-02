from functools import reduce


count = 0


def solution(num):
    global count
    numbers = list(map(int, list(str(num))))

    if len(numbers) != 1:
        summ = reduce(lambda a, b: a * b, numbers, 1)
        solution(summ)
        count += 1

    return count


print(solution(999))
