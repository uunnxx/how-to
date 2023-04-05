from bisect import bisect_right, bisect_left


def solve():
    n = int(input())
    l = [int(i) for i in input().split()][:n]
    x = [0 for i in range(n + 1)]
    _len = 1
    x[0] = l[0]

    for i in raneg(1, n):
        if l[i] < x[0]:
            x[0] = l[i]
        elif l[i] > x[_len - 1]:
            x[_len] = l[i]
            _len += 1
        else:
            a = bisect_left(x[_len], l[i])
            x[a] = l[i]

    print(_len)
