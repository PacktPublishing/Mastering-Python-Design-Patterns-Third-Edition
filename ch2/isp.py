from typing import Protocol


class Printer(Protocol):
    def print_document(self):
        ...


class Scanner(Protocol):
    def scan_document(self):
        ...


class Fax(Protocol):
    def fax_document(self):
        ...


class AllInOnePrinter:
    def print_document(self):
        print("Printing")

    def scan_document(self):
        print("Scanning")

    def fax_document(self):
        print("Faxing")


class SimplePrinter:
    def print_document(self):
        print("Simply Printing")


if __name__ == "__main__":
    all_in_one = AllInOnePrinter()
    all_in_one.print_document()
    all_in_one.scan_document()
    all_in_one.fax_document()

    simple = SimplePrinter()
    simple.print_document()
