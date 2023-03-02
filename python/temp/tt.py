# class Main():
#     def init(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_data(self):
#         print(f"{self.name=} {self.age=}")
#
#     def set_name(self, value):
#         self.name = value
#
#     def set_age(self, value):
#         self.age = value
#
#
# obj = Main()
#
# obj.init('Andrey', 22)
#
# obj.get_data()
#
# obj.set_name('Zorin')
# obj.set_age(200)
#
# obj.get_data()


class Main():
    def __init__(self, name, age):
        self.name = name
        self.age = age


obj = Main('Andrey', 22)

# Getter
print(obj.name)
print(obj.age)

# Setter
obj.name = 'Zorin'
obj.age = 22

# Getter
print(obj.name)
print(obj.age)
