MINI14 = "1.4GHz Mac mini"


class MacBuilder:
    class MacMini14:
        def __init__(self):
            self.memory = 4
            self.hdd = 500
            self.gpu = "Intel HD Graphics 5000"

        def __str__(self):
            info = (
                f"Model: {MINI14}",
                f"Memory: {self.memory}GB",
                f"Hard Disk: {self.hdd}GB",
                f"Graphics Card: {self.gpu}",
            )
            return "\n".join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print(f"I don't know how to build {model}")


if __name__ == "__main__":
    mb = MacBuilder()
    mac_mini = mb.build_computer(MINI14)
    print(mac_mini)
