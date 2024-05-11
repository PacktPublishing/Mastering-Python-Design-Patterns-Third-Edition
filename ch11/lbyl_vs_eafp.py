import os


def test_open_file(filename):
    if os.path.exists(filename):
        with open(filename) as f:
            print(f.text)
    else:
        print("No file there")


def better_test_open_file(filename):
    try:
        with open(filename) as f:
            print(f.text)
    except FileNotFoundError:
        print("No file there")


if __name__ == "__main__":
    filename = "no_file.txt"
    test_open_file(filename)
    better_test_open_file(filename)
