class Bird:
    def fly(self):
        print("I can fly")


class FlightlessBird(Bird):
    def fly(self):
        raise NotImplementedError("Can't fly")


class Penguin(FlightlessBird):
    pass


if __name__ == "__main__":
    brd = Bird()
    brd.fly()

    pgn = Penguin()
    try:
        pgn.fly()
    except Exception as e:
        print(f"Error: {e}")
