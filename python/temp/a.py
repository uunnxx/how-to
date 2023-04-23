class Nikolay:
    def __init__(self, name, age):
        if name == 'Николай':
            self.name = f"Меня зовут {name}"
        else:
            self.name = f"Меня зовут не {name}, а Николай!"


p1 = Nikolay('Женя', 22)
p2 = Nikolay('Николай', 30)

p1.surname = 'Бордиевич'
p2.surname = 'Анатолиевич'

print(p1.name)
print(p1.surname)

print(p2.name)
print(p2.surname)


