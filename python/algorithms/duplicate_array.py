from collections import Counter, namedtuple


def find_duplicate(nums):
    print(f"\n{nums}\n")

    for num in nums:
        current = nums[abs(num)]
        if current > 0:
            nums[abs(num)] = -current
        else:
            print(f"Repetition found: {abs(num)}")

    print()
    print(nums)


def find_duplicate2(nums):
    # hash_ = namedtuple('hash', ['index', 'value', 'occurance'])
    hashify: dict = {}
    a = Counter(nums)
    print(a)

    for o, v in a.items():
        if v > 1:
            print(o)

    for i in nums:
        if hashify.get(i, None):
            hashify[i] += 1
        else:
            hashify[i] = 1

    # for i, v in enumerate(nums):
    #     if not hashify.get(n, None):
    #         hashify[n] = 1
    #     else:
    #         hashify[n] += 1
    #
    #
    print(hashify.items())


if __name__ == '__main__':
    n = [1, 2, 4, 4, 5, 6, 6]
    # find_duplicate(n)
    find_duplicate2(n)



