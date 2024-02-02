import pickle


class Quote:
    def __init__(self, text, author):
        self.text = text
        self.author = author

    def save_state(self):
        current_state = pickle.dumps(self.__dict__)

        return current_state

    def restore_state(self, memento):
        previous_state = pickle.loads(memento)

        self.__dict__.clear()
        self.__dict__.update(previous_state)

    def __str__(self):
        return f"{self.text}\n- By {self.author}."


def main():
    print("** Quote 1 **")
    q1 = Quote(
        "A room without books is like a body without a soul.",
        "Unknown author",
    )
    print(f"\nOriginal version:\n{q1}")
    q1_mem = q1.save_state()

    # Now, we found the author's name
    q1.author = "Marcus Tullius Cicero"
    print(f"\nWe found the author, and did an updated:\n{q1}")

    # Restoring previous state (Undo)
    q1.restore_state(q1_mem)
    print(f"\nWe had to restore the previous version:\n{q1}")

    print()
    print("** Quote 2 **")
    text = (
        "To be you in a world that is constantly \n"
        "trying to make you be something else is \n"
        "the greatest accomplishment."
    )
    q2 = Quote(
        text,
        "Ralph Waldo Emerson",
    )
    print(f"\nOriginal version:\n{q2}")
    _ = q2.save_state()

    # changes to the text
    q2.text = (
        "To be yourself in a world that is constantly \n"
        "trying to make you something else is the greatest \n"
        "accomplishment."
    )
    print(f"\nWe fixed the text:\n{q2}")
    q2_mem2 = q2.save_state()

    q2.text = (
        "To be yourself when the world is constantly \n"
        "trying to make you something else is the greatest \n"
        "accomplishment."
    )
    print(f"\nWe fixed the text again:\n{q2}")

    # Restoring previous state (Undo)
    q2.restore_state(q2_mem2)
    print(f"\nWe restored the 2nd version, the correct one:\n{q2}")


if __name__ == "__main__":
    main()
