class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height


class BetterRectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    r = Rectangle(5, 6)
    print("Direct access of protected members")
    print(f"Rectangle area: {r._width * r._height} m2")

    r = BetterRectangle(5, 6)
    print("Recommended: Access via the public interface")
    print(f"Rectangle area: {r.area()} m2")
