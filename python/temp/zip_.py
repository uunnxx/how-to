# zip_longest implementation (already implemented in `itertools.zip_longest`)

def zip(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
        ])
    return result


print(zip(['a', 'b'], [1, 2], [True, False]))  # [['a', 1, True], ['b', 2, False]]
print(zip(['a'], [1, 2], [True, False]))  # [['a', 1, True], [None, 2, False]]
print(zip(['a'], [1, 2], [True, False], fill_value='_'))  # [['a', 1, True], ['_', 2, False]]
