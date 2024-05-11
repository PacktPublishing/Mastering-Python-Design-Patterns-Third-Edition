def manipulate(mylist=[]):
    mylist.append("test")
    return mylist


def better_manipulate(mylist=None):
    if not mylist:
        mylist = []

    mylist.append("test")
    return mylist


if __name__ == "__main__":
    print("function manipulate()")
    print(manipulate())
    print(manipulate())
    print(manipulate())

    print("function better_manipulate()")
    print(better_manipulate())
    print(better_manipulate())
