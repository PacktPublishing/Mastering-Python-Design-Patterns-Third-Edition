class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def calculate_area(shape):
    return shape.area()


if __name__ == "__main__":
    rect = Rectangle(12, 8)
    print(calculate_area(rect))
