def br():
    print(f"\n{'-' * 80}\n")


class Arcade:
    pass


arcade = Arcade()


class Person:
    '''Defines a person by name'''

    def __init__(self, fname: str, mname: str = None, lname: str = None):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def full_name(self) -> str:
        """This method returns the person's full name"""
        full_name = self.fname
        if self.mname:
            full_name = f"{full_name} {self.mname}"
        if self.lname:
            full_name = f"{full_name} {self.lname}"

        return full_name


p1 = Person('George', 'James', 'Smith')
print(p1.full_name())

br()


def main():
    # Create some people
    people = [
        Person('John', 'George', 'Smith'),
        Person('Bill', lname='Thompson'),
        Person('Sam', mname='Watson'),
        Person('Tom')
    ]

    # Print out the full names of the people
    for person in people:
        print(person.full_name())


main()


br()


# |---------------------------------|
# | + Rectangle                     |
# | + x: int                        |
# | + y: int                        |
# | + width: int                    |
# | + height: int                   |
# | + pen_color: tuple              |
# | + fill_color: tuple             |
# | + dir_x: int                    |
# | + dir_y: int                    |
# | + speed_x: int                  |
# | + speed_y: int                  |
# |---------------------------------|
# | + __init__(): None              |
# | + set_pen_color(): Rectangle    |
# | + set_fill_color(): Rectangle   |
# | + draw(): None                  |
# |---------------------------------|

# The UML diagram shows the attributes encapsulated in the class necessary
# to render a rectangle on-screen. All of these attributes are initialized
# during the construction of a Rectangle object:

# - x, y, width, height - define the position of the Rectangle on screen
# and teh dimensions to use when drawing it
# - pen_color, fill_color - define the colors used to outline the Rectangle
# and fill it
# - dir_x, dir_y - the direction of movement relative to the screen x and y
# axes, these are either 1 or -1
# - speed_x, speed_y - the speed at which the Rectangle is moving in pixels
# per update
# - The diagram also includes the definition of three methods the class
# supports:
# - set_pen_color() - provides a mechanism to set the pen color used to draw
# the rectangle instance object
# - set_fill_color() - provides a mechanism to set the fill color used to fill
# a rectangle instance object
# - draw() - draws a Rectangle object instance on the screen

COLOR_PALETTE = []


class Rectangle:
    """This class defines a simple rectangle object"""

    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            pen_color: tuple = COLOR_PALETTE[0],
            fill_color: tuple = COLOR_PALETTE[1],
            dir_x: int = 1,
            dir_y: int = 1,
            speed_x: int = 1,
            speed_y: int = 1
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pen_color = pen_color
        self.fill_color = fill_color
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def set_pen_color(self, color: tuple) -> Rectangle:
        """
        Set the pen color of the rectangle

        Arguments:
            color {tuple} -- the color tuple to set the rectangle pen to

        Returns:
            Rectangle -- returns self for chaining
        """
        self.pen_color = color
        return self

    def set_fill_color(self, color: tuple) -> Rectangle:
        """
        Set the fill color of the Rectangle

        Arguments:
            color {tuple} -- the color tuple to set the rectangle fill to

        Returns:
            Rectangle -- returns self for chaining
        """
        self.fill_color = color
        return self

    def draw(self):
        """Draw the rectangle based on the current state"""
        arcade.draw_xywh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.fill_color
        )
        arcade.draw_xywh_rectangle_outline(
            self.x, self.y, self.width, self.height, self.pen_color, 3
        )
