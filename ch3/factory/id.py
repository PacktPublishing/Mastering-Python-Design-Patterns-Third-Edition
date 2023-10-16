class MyClass:
    pass


if __name__ == "__main__":
    a = MyClass()
    b = MyClass()

    print(id(a) == id(b))
    print(id(a))
    print(id(b))
