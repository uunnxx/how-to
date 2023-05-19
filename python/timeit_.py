import timeit
import time


def _timeit(func):
    start = time.perf_counter()

    func()

    return (time.perf_counter() - start)


def _timeit_dec(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(time.perf_counter() - start)
        return result
    return wrapper


@_timeit_dec
def one():
    lst = []
    for i in range(10**4):
        if i % 2 == 0:
            lst.append(i)

    return lst


def two():
    lst = [x for x in range(10**4) if x % 2 == 0]

    return lst


one()

print(_timeit(one))
print(_timeit(two))

print(timeit.timeit(stmt=one, number=1000))
print(timeit.timeit(stmt=two, number=1000))
