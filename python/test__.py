# inputs = input().split()
# a, b = map(int, inputs)
#
# print(a, b)


# class Greetings:
#     def __init__(self, default_name):
#         self.default_name = default_name
#
#     def greet(self, name=None):
#         """docstring for greet"""
#         return f"Hello, {name if name else self.default_name}"
#
#
# g = Greetings('Alan')
# print(g.greet())


class Temperature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale

    def __repr__(self):
        return f"Temperature ({self.value}, {self.scale})"

    def __str__(self):
        return f"Temperature {self.value}^ {self.scale}"

    def main(self):
        return 0


# t = Temperature(25, 'C')
# print(repr(t))
# print(str(t))
# print(t)
#
#
#


import inspect

class MonkeyPatch:
    def __init__(self, n1) -> None:
        self.n1 = n1

    def add(self, other):
        return (self.n1 + other)


obj = MonkeyPatch(10)
obj.add(20)
print(inspect.getmembers(obj, predicate=inspect.ismethod))
