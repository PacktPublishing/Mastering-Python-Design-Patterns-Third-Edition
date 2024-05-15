class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author


class BetterBook:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def presentation_line(self):
        return f"{self._title} by {self._author}"


if __name__ == "__main__":
    b1 = Book(
        "Mastering Object-Oriented Python",
        "Steven F. Lott",
    )
    print("Bad practice: Direct access of protected members")
    print(f"{b1._title} by {b1._author}")

    b2 = BetterBook(
        "Python Algorithms",
        "Magnus Lie Hetland",
    )
    print("Recommended: Access via the public interface")
    print(b2.presentation_line())
