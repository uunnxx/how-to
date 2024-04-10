class Person:
    def __init__(self, name, age):  # Initialiser
        self.name = name  # Attribute
        self.age = age  # Attribute

    def say_hello(self) -> str:
        return f'Hi {self.name}!'

    def increase_age_by_one(self) -> None:
        self.age += 1
        return True  # write the logic which will check is it ok to change by one

    def change_age(self, new_age: int) -> bool:
        if isinstance(new_age, int) and (100 > new_age > 0):
            self.age = new_age

    def change_name(self, new_name: str) -> bool:
        self.name = new_name
        return True  # write the logic where you'll check if it's ok

        # if isinstance(new_name, str):
        #     self.name = new_name




    def __str__(self) -> str:
        return f'{self.__class__.__name__}:\n\tname: {self.name}\n\tage: {self.age}'




# person = Person('John', 100)

# print(person)
# print(person.say_hello())
# person.increase_age_by_one()
# print(person)


# print()
# for i in object.__class__.__dict__:
#     print(i)



class Car:
    def __init__(self, model, colors):
        self.model = model
        self.colors: list[str] = []
        for color in colors:
            self.colors.append(color.lower())

    def __contains__(self, color: str):
        return color.lower() in self.colors



car_a = Car('Astra', ['Red', 'Blue'])
car_b = Car('Focus', ['Red', 'Blue', 'Green', 'Yellow', 'White'])

print('Red' in car_a)
print('red' in car_a)
