class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn


class BetterBook:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn

    def presentation_line(self):
        return f"{self._title} by {self._author}"

    def details(self):
        return {
            "name": self._title,
            "author": self._author,
            "isbn": self._isbn,
        }


if __name__ == "__main__":
    b1 = Book(
        "Mastering Object-Oriented Python",
        "Steven F. Lott",
        "9781789531367",
    )
    print(
        "Bad practice: Direct access of protected members"
    )
    print(b1._title, b1._author, b1._isbn)

    b2 = BetterBook(
        "Python Algorithms",
        "Magnus Lie Hetland",
        "9781484200568",
    )
    print(
        "Recommended: Access via the public interface"
    )
    print(b2.presentation_line())
    print("All details:")
    details = b2.details()
    for key in details:
        print(f"  {key}: {details[key]}")
