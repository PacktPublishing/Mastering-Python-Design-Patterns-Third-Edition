class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative!")
        self._radius = value


if __name__ == "__main__":
    circle = Circle(10)
    print(circle.radius)

    # Now, we decided to update the radius
    circle.radius = 15
    print(circle.radius)