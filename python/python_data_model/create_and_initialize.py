import uuid


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        # print(cls)
        # print(args)
        # print(kwargs)

        # if len(args) < 2:
        #     raise TypeError('You have not supplied the correct number of args')
        # return super().__new__(cls, args, kwargs)
        
        # name, age = args
        #
        # if not isinstance(name, str):
        #     raise TypeError('Your name should be string')
        #
        # if not isinstance(age, (int, float)):
        #     raise TypeError('Your age should be a numeric type')
        #
        # return super().__new__(cls)
        obj = super().__new__(cls)
        obj.uuid = uuid.uuid4()

        return obj

        


# person = Person('Mike', 28)
person = Person('Mike', 28)
