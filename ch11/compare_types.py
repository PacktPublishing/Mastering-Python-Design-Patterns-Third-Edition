from collections import UserList


class CustomListA(UserList):
    pass


class CustomListB(UserList):
    pass


def compare(obj):
    if type(obj) in (CustomListA, CustomListB):
        print("It's a custom list!")
    else:
        print("It's a something else!")


def better_compare(obj):
    if isinstance(obj, UserList):
        print("It's a custom list!")
    else:
        print("It's a something else!")


if __name__ == "__main__":
    obj1 = CustomListA([1, 2, 3])
    obj2 = CustomListB(["a", "b", "c"])

    compare(obj1)
    compare(obj2)
    better_compare(obj1)
    better_compare(obj2)
