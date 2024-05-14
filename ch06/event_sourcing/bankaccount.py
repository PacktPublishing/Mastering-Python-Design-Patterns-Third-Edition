class Account:
    def __init__(self):
        self.balance = 0
        self.events = []

    def apply_event(self, event):
        if event["type"] == "deposited":
            self.balance += event["amount"]
        elif event["type"] == "withdrawn":
            self.balance -= event["amount"]
        self.events.append(event)

    def deposit(self, amount):
        event = {"type": "deposited", "amount": amount}
        self.apply_event(event)

    def withdraw(self, amount):
        event = {"type": "withdrawn", "amount": amount}
        self.apply_event(event)


def main():
    account = Account()
    account.deposit(100)
    account.deposit(50)
    account.withdraw(30)
    account.deposit(30)

    for evt in account.events:
        print(evt)
    print(f"Balance: {account.balance}")


if __name__ == "__main__":
    main()
