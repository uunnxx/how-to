class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Overloading add (+) operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return MyPoint(x, y)

    # Overloading < operator
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


p1 = MyPoint(1, 2)
p2 = MyPoint(3, 4)

print(p1)
print(p2)

print(p1 + p2)
print(p1 < p2)
