class Person:
    name = 'Andrew'
    age = 40

    def info(self):
        print(f"My name is {self.name} and I'm {self.age} old")


person = Person()
# person.info()


class Person1:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def info(self):
        print(f"My name is {self.name} and I'm {self.age} old")


person1 = Person1('Andrew', 22)
person2 = Person1('John', 24)
person3 = Person1('Bone', 22)

for person in [person1, person2, person3]:
    person.info()

