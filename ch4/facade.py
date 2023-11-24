from enum import Enum

State = Enum(
    "State",
    "NEW RUNNING SLEEPING RESTART ZOMBIE",
)


class User:
    pass


class Process:
    pass


class File:
    pass


class FileServer:
    def __init__(self):
        """actions for initializing the file server"""
        self.name = "FileServer"
        self.state = State.NEW

    def boot(self):
        """actions for booting the file server"""
        print(f"booting the {self}")
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions for killing the file server"""
        print(f"Killing {self}")
        self.state = (
            State.RESTART if restart else State.ZOMBIE
        )

    def create_file(self, user, name, perms):
        """check validity of permissions, user rights, etc."""
        msg = (
            f"trying to create file '{name}' "
            f"for user '{user}' "
            f"with permissions {perms}"
        )
        print(msg)


class ProcessServer:
    def __init__(self):
        """actions for initializing the process server"""
        self.name = "ProcessServer"
        self.state = State.NEW

    def boot(self):
        """actions for booting the process server"""
        print(f"booting the {self}")
        self.state = State.RUNNING

    def kill(self, restart=True):
        """actions for killing the process server"""
        print(f"Killing {self}")
        self.state = (
            State.RESTART if restart else State.ZOMBIE
        )

    def create_process(self, user, name):
        """check user rights, generate PID, etc."""
        msg = (
            f"trying to create process '{name}' "
            f"for user '{user}'"
        )
        print(msg)


class WindowServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:
    """The Facade"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, perms):
        return self.fs.create_file(user, name, perms)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file("foo", "hello.txt", "-rw-r-r")
    os.create_process("bar", "ls /tmp")


if __name__ == "__main__":
    main()
