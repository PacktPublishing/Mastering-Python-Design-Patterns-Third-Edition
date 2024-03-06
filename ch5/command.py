import logging
import os

logging.basicConfig(level=logging.DEBUG)


class RenameFile:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        logging.info(f"[renaming '{self.src}' to '{self.dest}']")
        os.rename(self.src, self.dest)

    def undo(self):
        logging.info(f"[renaming '{self.dest}' back to '{self.src}']")
        os.rename(self.dest, self.src)


class CreateFile:
    def __init__(self, path, txt="hello world\n"):
        self.path = path
        self.txt = txt

    def execute(self):
        logging.info(f"[creating file '{self.path}']")
        with open(self.path, mode="w", encoding="utf-8") as out_file:
            out_file.write(self.txt)

    def undo(self):
        logging.info(f"deleting file {self.path}")
        os.remove(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        logging.info(f"[reading file '{self.path}']")
        with open(self.path, mode="r", encoding="utf-8") as in_file:
            print(in_file.read(), end="")


def main():

    orig_name, new_name = "file1", "file2"

    commands = (
        CreateFile(orig_name),
        ReadFile(orig_name),
        RenameFile(orig_name, new_name),
    )

    for c in commands:
        c.execute()

    answer = input("reverse the executed commands? [y/n] ")

    if answer not in "yY":
        print(f"the result is {new_name}")
        exit()

    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            logging.error(str(e))


if __name__ == "__main__":
    main()
