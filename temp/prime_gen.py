from __future__ import print_function


def prime(n):
    if n < 2:
        print('Integer must be >= 2')
        return 0

    p = 2

    while n > 0:
        for x in range(2, p):
            if p % x == 0:
                break
        else:
            yield p
            n -= 1
        p += 1


p = prime(1)
next(p)

# p = prime(3)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

# for x in prime(100):
#     print(x, end=" ")
