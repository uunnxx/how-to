def unique_in_order(iterable):
    result = []
    for i in iterable:
        if not result:
            result.append(i)
            continue
        if result[-1] == i:
            continue
        result.append(i)
    return result


def unique_in_order2(iterable):
    result = []
    prev = None
    for char in iterable:
        if char != prev:
            result.append(char)
            prev = char
    return result


print(unique_in_order('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order('ABBCcAD'))          # == ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order([1, 2, 2, 3, 3]))    # == [1,2,3]

print('-' * 40)

print(unique_in_order2('AAAABBBCCDAABBB'))  # == ['A', 'B', 'C', 'D', 'A', 'B']
print(unique_in_order2('ABBCcAD'))          # == ['A', 'B', 'C', 'c', 'A', 'D']
print(unique_in_order2([1, 2, 2, 3, 3]))    # == [1,2,3]
