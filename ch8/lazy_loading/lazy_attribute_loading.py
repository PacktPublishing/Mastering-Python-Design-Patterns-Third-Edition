class LazyLoadedData:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            self._data = self.load_data()
        return self._data

    def load_data(self):
        print("Loading expensive data...")
        return sum(i * i for i in range(100000))


def main():
    obj = LazyLoadedData()
    print("Object created, expensive attribute not loaded yet.")

    # The expensive operation will occur only when the attribute is accessed for the first time
    print("Accessing expensive attribute:")
    print(obj.data)
    print("Accessing expensive attribute again, no reloading occurs:")
    print(obj.data)


if __name__ == "__main__":
    main()
