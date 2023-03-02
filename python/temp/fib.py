from typing import Iterator


def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


def fib2(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
