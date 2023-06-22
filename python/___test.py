from functools import partial


def power_to(to: int, x: int) -> int:
    if x < 0:
        return abs(x)**to
    return x**to


square = partial(power_to, 2)
cube = partial(power_to, 3)


def solution(lst):
    squared = sorted(map(square, lst))
    cubed = sorted(map(cube, lst))
    return [squared, cubed]


lst1 = [1, 2, 3]
lst2 = [-6, -4, -2, 1, 3]

print(solution(lst1))
print(solution(lst2))
