from typing import Protocol, runtime_checkable


@runtime_checkable
class MessageSender(Protocol):
    def send(self, message: str):
        ...


class Email:
    def send(self, message: str):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def send(self, message: str):
        self.sender.send(message)


if __name__ == "__main__":
    email = Email()
    notif = Notification(sender=email)
    notif.send(message="This is the message.")