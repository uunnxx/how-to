def rand_shift(nums, rand):
    shifted_nums = []
    for num in nums:
        shifted = num + rand.randrange(-10, 11)
        if shifted > 0:
            shifted_nums.append(shifted)

    return shifted_nums


def rand_shift2(nums, rand):
    return list(filter(lambda shifted: shifted > 0,
                       map(lambda num: num + rand.randrange(-10, 11), nums)))


def rand_shift3(nums, rand):
    return [shifted for shifted in (num + rand.randrange(-10, 11) for num in nums)]


def abs(num: int | float) -> int | float:
    return num if num > 0 else -num
