from functools import wraps, cache
from time import perf_counter
import sys


def memoize(func):
    cache: dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key: str = str(args) + str(kwargs)

        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]

    return wrapper


@memoize
def fib(n) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


@cache
def fib2(n) -> int:
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    sys.setrecursionlimit(10**4)
    calc_fib = 3000
    start: float = perf_counter()
    fib_res: int = fib(calc_fib)
    end: float = perf_counter()

    start2: float = perf_counter()
    fib_res2: int = fib2(calc_fib)
    end2: float = perf_counter()

    print(f"\n\tCalculating {calc_fib} fibbonaci with custom memoize took: {round(end - start, 3)} seconds")

    print(f"\n\tCalculating {calc_fib} fibbonaci with functools' cache took: {round(end2 - start2, 3)} seconds")
