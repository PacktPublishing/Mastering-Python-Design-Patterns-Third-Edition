from typing import Protocol


class Sender(Protocol):
    def send(self, message):
        ...


class EmailSender:
    def send(self, message):
        print(f"Sending email: {message}")


class SMSSender:
    def send(self, message):
        print(f"Sending SMS: {message}")


class MessageService:
    def __init__(self, sender: Sender):
        self.sender = sender

    def send_message(self, message):
        self.sender.send(message)


if __name__ == "__main__":
    email_service = MessageService(EmailSender())
    email_service.send_message("Hello via Email")

    sms_service = MessageService(SMSSender())
    sms_service.send_message("Hello via SMS")
