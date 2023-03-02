def br():
    print()
    print('-' * 80)
    print()

a = [1, 2, 3]
b = a

print(a)
print(b)

print(f'a == b: {a == b}')
print(f'a is b: {a is b}')
c = list(a)

print(c)
print(f'a is c: {a is c}')

br()

# Representing strings: `__repr__`


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


my_car = Car('Red', 37281)

print(my_car)
print(my_car.color, my_car.mileage)


br()


class Car2:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'{self.color} machine'


my_car2 = Car2('Red', 37281)

print(my_car2)


br()
