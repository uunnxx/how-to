def max_sequence(arg):
    max_sum = 0
    current = 0
    for i in arg:
        current += i
        current = max(current, 0)
        max_sum = max(max_sum, current)
            # or
            # max_sum = max(max_sum, current)

    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
# should be 6: [4, -1, 2, 1]
