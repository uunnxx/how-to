given = 12340


def solution(nums: int) -> int:

    def _compute(num: int):
        reversed = 0
        remainder = 0

        while num > 0:
            remainder = num % 10
            num = num // 10
            reversed = reversed * 10 + remainder

        return reversed

    if nums < 0:
        return int('-' + str(_compute(abs(nums))))

    return _compute(nums)


def solution2(num: int) -> int:
    if num > 0:
        return int(str(num)[::-1])

    return int('-' + str(num)[:0:-1])


print(solution(given))
print(solution2(given))
