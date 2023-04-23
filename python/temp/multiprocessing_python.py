import os

from multiprocessing import Pool
from multiprocessing import Process


def f(x: int) -> int:
    return x**2


def m(name: str) -> None:
    print(f"Hello {name.title()}")


if __name__ == '__main__':
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))
    p = Process(target=m, args=('bob',))
    p.start()
    p.join()
