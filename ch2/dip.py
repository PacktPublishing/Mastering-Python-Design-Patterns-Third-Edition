from typing import Protocol


class MessageSender(Protocol):
    def send(self, message: str):
        ...


class Email:
    def send(self, message: str):
        print(f"Sending email: {message}")


class Notification:
    def __init__(self, sender: MessageSender):
        self.sender: MessageSender = sender

    def send(self, message: str):
        self.sender.send(message)


if __name__ == "__main__":
    email: Email = Email()
    notif: Notification = Notification(sender=email)
    notif.send(message="This is the message.")
