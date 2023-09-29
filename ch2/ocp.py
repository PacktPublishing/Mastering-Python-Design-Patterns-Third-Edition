import math


class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)


def calculate_area(shape):
    return shape.area()


if __name__ == "__main__":
    rect = Rectangle(12, 8)
    print("Rectangle area")
    print(calculate_area(rect))

    print("Circle area")
    circ = Circle(11)
    print(calculate_area(circ))
