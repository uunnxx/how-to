def reverse2(x: int) -> int:
    if x < 0:
        res = int('-' + str(abs(x))[::-1])
        print('negative: ', res)
        return res if (res >= -2**31) else 0
    else:
        res = int(str(x)[::-1])
        print('positive: ', res)
        return res if (res <= (2**31 - 1)) else 0



print(reverse2(123))
