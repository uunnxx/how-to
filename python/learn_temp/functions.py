def specila_multiplication(string: str) -> str:
    for i, e in enumerate(string):
        print(e * (i+1), end='')
    print()


specila_multiplication('abcxf')



def my_max6(a, b, c, d, e, f) -> int:
    return max(a, b, c, d, e, f)


print(my_max6(1, 2, 3, 4, 5, 6))


def fib(n: int) -> list:
    fibs = [0, 1]

    if n == 1:
        return fibs[0]
    if n == 2:
        return fibs[1]

    for i in range(n):
        fibs.append(fibs[-2] + fibs[-1])
        fibs.append(fibs[-2] + fibs[-1])

    return fibs


print(fib(4))
