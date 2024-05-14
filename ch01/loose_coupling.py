class MessageService:
    def __init__(self, sender):
        self.sender = sender

    def send_message(self, message: str):
        self.sender.send(message)


class EmailSender:
    def send(self, message: str):
        print(f"Sending email: {message}")


class SMSSender:
    def send(self, message: str):
        print(f"Sending SMS: {message}")


if __name__ == "__main__":
    email_service = MessageService(EmailSender())
    email_service.send_message("Hello via Email")

    sms_service = MessageService(SMSSender())
    sms_service.send_message("Hello via SMS")
