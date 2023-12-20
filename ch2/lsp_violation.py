class Bird:
    def fly(self):
        print("I can fly")


class Penguin(Bird):
    def fly(self):
        print("I can't fly")


# Function that expects a Bird object
def make_bird_fly(bird):
    bird.fly()


# Using the classes
if __name__ == "__main__":
    generic_bird = Bird()
    penguin = Penguin()

    make_bird_fly(generic_bird)
    make_bird_fly(penguin)
