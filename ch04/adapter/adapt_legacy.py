class OldPaymentSystem:
    def __init__(self, currency):
        self.currency = currency

    def make_payment(self, amount):
        print(
            f"[OLD] Pay {amount} {self.currency}"
        )


class NewPaymentGateway:
    def __init__(self, currency):
        self.currency = currency

    def execute_payment(self, amount):
        print(
            f"Execute payment of {amount} {self.currency}"
        )


class PaymentAdapter:
    def __init__(self, system):
        self.system = system

    def make_payment(self, amount):
        self.system.execute_payment(amount)


def main():
    old_system = OldPaymentSystem("euro")
    print(old_system)
    new_system = NewPaymentGateway("euro")
    print(new_system)

    adapter = PaymentAdapter(new_system)
    adapter.make_payment(100)


if __name__ == "__main__":
    main()
