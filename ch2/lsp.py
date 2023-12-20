class Bird:
    def move(self):
        print("I'm moving")


class FlyingBird(Bird):
    def move(self):
        print("I'm flying")


class FlightlessBird(Bird):
    def move(self):
        print("I'm walking")


# Function that expects a Bird object
def make_bird_move(bird):
    bird.move()


# Using the classes
if __name__ == "__main__":
    generic_bird = Bird()
    eagle = FlyingBird()
    penguin = FlightlessBird()

    make_bird_move(generic_bird)
    make_bird_move(eagle)
    make_bird_move(penguin)
