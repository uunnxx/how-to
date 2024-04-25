from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Lin(Computer):
    def __init__(self):
        print('a')
        
    def process(self):
        # return super().process()
        pass



# comp = Computer()
# comp.process()

# comp = Lin()



class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


point = Point()
point.set_coords(1, 2)

# print(point.__dict__)


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y



class Point:
    def __new__(cls, *args, **kwargs):
        print(f'calling __new__ for {cls}')
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f'calling __init__ for {self}')
        self.x = x
        self.y = y


point = Point(1, 2)
print(point)


class Vector:
    def __init__(self, *args):
        self.values = args

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item < len(self.values):
            return self.values[item]
        else:
            raise IndexError

    # index + 1
    # def __getitem__(self, item):
    #     if 1 <= item <= len(self.values):
    #         return self.values[item - 1]
    #     else:
    #         raise IndexError

    def __settitem__(self, key, value):
        if 0 <= key < len(self.values):
            self.values[key] = value
        else:
            raise IndexError

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError

