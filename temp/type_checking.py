def odd(n: int) -> bool:
    return n % 2 != 0


odd(3)
odd(4)

# odd('test')

#
# class Point:
#     def __init__(self):
#         pass
#
#     def reset(self):
#         self.x = 0
#         self.y = 0
#
# p = Point()
# Point.reset(p)
# p.reset()
# print(p.x, p.y)


import math

class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(point1))
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)
point1.move(3, 4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

point = Point()
point.x = 5
print(point.x)
# print(point.y)


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self) -> None:
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

point = Point(3, 5)
print(point.x, point.y)


class Point:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.move(x, y)


class Point:
    def __init__(
        self,
        x: float = 0,
        y: float = 0
    ) -> None:
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Point:
    """
    Represents a point in two-demensional geometric coordinates

    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        """
        Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the point
        defaults to the origin.

        :param x: float x-coordinate
        :param y: float y-coordinate
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move teh point to a new location in 2D space.

        :param x: float x-coordinate
        :param y: float y-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def calculate_distance(self, other: 'Point') -> float:
        """
        Calculate the Euclidean distance from this point
        to a second point passed as a parameter.

        :param other: Point instance
        :return: float distance
        """
        return math.hypot(self.x - other.x, self.y - other.y)



