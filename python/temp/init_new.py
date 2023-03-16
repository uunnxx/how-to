class Point:
    def __init__(self, data):
        self.num = data

    def print_num(self):
        print(self.num)


obj = Point(100)
obj.print_num()


class Person:
    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        self.instance_method()

    def instance_method(self):
        print('success!')


personObj = Person()


# You can actually use
# super().method_name(*args, **kw)  # PEP 3135
# In this case, it can be
# super().__new__(cls, *args, **kw)
# The cls is actually necessary for __new__.
