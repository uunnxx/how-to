class Vector():
    def __new__(cls, x, y):
        print('__new__ was invoked')
        instance = object.__new__(cls)
        return instance


    def __init__(self, x, y):
        print('__init__ was invoked')
        self.x = x
        self.y = y


vector1 = Vector(12, 8)
