from typing import Iterable, Iterator


lst: list = [44, 77, 11, 22, 33]

itr: Iterable = iter(lst)

# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# itr.__next__()  # StopIteration


class PowOfTwo:
    """
    Class to implement an iterator of powers of two
    """

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


print(PowOfTwo.__doc__)
a = PowOfTwo(4)
itr: Iterable = iter(a)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
#


some_lst = [i for i in range(1, 6)]
