from collections import defaultdict
from collections import Counter


def counter(lst: list) -> dict:
    result = {}

    for element in lst:
        if result.get(element) is None:
            result[element] = 1
            continue

        result[element] += 1


    return result




def counter_dict(lst: list) -> dict:

    # result = defaultdict(lambda: 0)
    result = defaultdict(int)

    for element in lst:
        result[element] += 1

    return dict(result)


def counter_with_counter(lst: list) -> dict:
    return dict(Counter(lst))



print(counter([1, 2, 1, 3]))
print(counter_dict([1, 2, 1, 3]))
print(counter_with_counter([1, 2, 3, 1]))


assert counter([1, 2, 1, 3]) == {1: 2, 2: 1, 3: 1}
assert counter_dict([1, 2, 1, 3]) == {1: 2, 2: 1, 3: 1}
assert counter_with_counter([1, 2, 3, 1]) == {1: 2, 2: 1, 3: 1}
