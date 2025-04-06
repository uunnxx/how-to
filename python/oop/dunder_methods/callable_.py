from dataclasses import dataclass


def linear_model(a, b, x):
    return a * x + b

# out1 = linear_model(1, 5, 0)
# out2 = linear_model(5, 2, 3)
#
# print(out1)
# print(out2)


class LinearModel:
    a: int
    b: int

    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def compute(self, x: int):
        output: int = self.a * x + self.b
        return output


@dataclass
class LinearModel1:
    a: int
    b: int

    def compute(self, x: int):
        output: int = self.a * x + self.b
        return output


@dataclass
class LinearModel2:
    a: int
    b: int

    def compute(self, x: int) -> int:
        return self.a * x + self.b

    def __call__(self, x: int) -> int:
        return self.a * x + self.b



lm = LinearModel2(2, 3)

# out1 = lm.compute(0)
# out2 = lm.compute(10)

out1 = lm(0)
out2 = lm(10)

print(out1)
print(out2)


