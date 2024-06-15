class NonDataDescriptor:
    """Non-Data Descriptor (defines only getter)"""
    def __init__(self, initial_value=None, name='var'):
        self.val = initial_value
        self.name = name

    def __get__(self, obj, objtype):
        print(f'Retrieving {self.name}')
        return self.val



class DescriptorClass:
    """Data Descriptor (defines getter and setter"""
    def __init__(self, initial_value=None, name='var'):
        self.val = initial_value
        self.name = name

    def __get__(self, obj, objtype):
        print(f'Retrieving {self.name}')
        return self.val

    def __set__(self, obj, val):
        print(f'Setting {self.name}')
        self.val = val


class SimpleClass:
    x = DescriptorClass(1, 'variable "x"')
    y = 2


s = SimpleClass()
print(s.x)
print(s.y)
s.x = 3
print(s.x)
