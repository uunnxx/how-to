given: list[int] = [1, 2, 3, 4, 5]
# given: list[int] = [1, 2, 3, 4, 5, 6, 7]
k: int = 2


def rotate_k(lst: list[int], k: int) -> list[int]:
    """Rotate a list K times"""
    elements: int = len(lst)
    result: list[int] = []
    k = k % elements

    # we don't need to check (k == elements) 'cause (k = k % elements)
    # if k == 0 or k == elements:
    if k == 0:
        return lst
    # elif k > elements:

    result.extend(lst[-k:])
    result.extend(lst[0:-k])

    return result


print(rotate_k(given, k))
print(rotate_k(given, 7))
print(rotate_k(given, 0))
print(rotate_k(given, 10))
print(rotate_k(given, -2))


assert rotate_k(given, k), [4, 5, 1, 2, 3]
assert rotate_k(given, 7), [4, 5, 1, 2, 3]
assert rotate_k(given, 0), given
assert rotate_k(given, 10), given
assert rotate_k(given, -2), [3, 4, 5, 1, 2]
