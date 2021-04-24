"""Examples of object-oriented programming concepts."""

class Point:
    # Defining attributes (related variables)
    # of our class
    x: float = 0.0
    y: float = 0.0

    def __init__(self, x: float, y: float):
        """Construct a point by giving x and y arguments."""
        self.x = x
        self.y = y

    def invert(self) -> None:
        """A method to invert the attributes (swap) of the Point."""
        temp: float = self.x
        self.x = self.y
        self.y = temp

    def move_up(self, dy: float) -> None:
        """Increase the y attribute of an object."""
        self.y += dy


a: Point = Point(4.0, 5.0)
# a.x = 4.0
# a.y = 5.0
print(a.__repr__()) # The same as print(a)
a.invert()
print(a)
a.move_up(10.0)
print(a)


b: Point = Point(0.0, 0.0)
# assign attributes to an object:
b.x = 2.0
b.y = -1.0

