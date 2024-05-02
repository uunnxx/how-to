from typing import Callable


def mysum(a: int, b: int) -> int:
    return a + b


def process_operation(operation: Callable[
                      [int, int], int],
                      a: int, b: int) -> int:
    return operation(a, b)


print(process_operation(mysum, 1, 5))  # 6
