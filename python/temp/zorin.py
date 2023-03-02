l1 = [-7, 8, 11, -1, 3]
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def multply(a, b):
    for left, right in zip(a, b):
        yield left * right

def mul(zipped):
    yield zipped[0] * zipped[1]



print([map(mul, zip(l1, l2)) for _ in range(3)])



g = multply(l1, l2)

print(next(g))
print(next(g))
print(next(g))






def get_a(x):
    res = None if x < 0 else x ** 0.5
    return res, x


a, b = get_a(49)
print(a, b)



