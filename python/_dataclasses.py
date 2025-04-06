class Fruit:
    def __init__(self, name, quantity: int):
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return(
            f"{self.__class__.__name__}"
            "("
            f"name={self.name!r}, "
            f"quantity={self.quantity!r}"
            ")"
        )


apple: Fruit = Fruit('Apple', '10')


print(apple)

# print(list(apple.__dict__.items()))
#
#
# for a, v in apple.__dict__.items():
#     print(f"{a}={v}")


from dataclasses import dataclass


@dataclass
class Fruit2:
    name: str
    quantity: int


peach: Fruit2 = Fruit2('Peach', 20)

print(peach)
