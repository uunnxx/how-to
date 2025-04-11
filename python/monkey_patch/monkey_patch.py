import inspect
import request
import math


class MonkeyPatch:
    def __init__(self, n1):
        self.n1 = n1

    def add(self, other):
        return (self.n1 + other)


obj1 = MonkeyPatch(10)
obj1.add(20)

print(inspect.getmembers(obj1, predicate=inspect.ismethod))
