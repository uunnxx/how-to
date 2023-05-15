class Human:
    # attributes
    species = 'Homo Sapiens'

    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender


x = Human('Edcorner', 32, 'Male')
y = Human('Learny', 20, 'Female')


print(x.name)
print(y.name)




# Inheritance
# Encapsulation
# Polymorphism
# Abstraction of Data


# Inheritance
class Parent:
    pass


class Child(Parent):
    pass


class Human:

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender


class Boy(Human):

    def __init__(self, name: str, age: int):
        super().__init__(name, age, 'Male')

    def __str__(self):
        return f"{self.name} {self.age} {self.gender}"


class Girl(Human):

    def __init__(self, name: str, age: int):
        super().__init__(name, age, 'Female')

    def __str__(self):
        return f"{self.name} {self.age} {self.gender}"


john = Boy('John', 22)
print(john)

print(Boy.__mro__)
