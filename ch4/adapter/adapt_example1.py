# Legacy payment system
class OldPaymentSystem:
    def __init__(self, currency):
        self.currency = currency

    def make_payment(self, amount):
        print(f"Making payment of {amount} {self.currency} using the old system.")


# New payment gateway
class NewPaymentGateway:
    def __init__(self, currency):
        self.currency = currency

    def execute_payment(self, amount):
        print(f"Executing payment of {amount} {self.currency} using the new gateway.")


# Adapter
class PaymentAdapter:
    def __init__(self, system):
        self.system = system

    def make_payment(self, amount):
        self.system.execute_payment(amount)


if __name__ == "__main__":
    old_system = OldPaymentSystem("euro")
    new_system = NewPaymentGateway("euro")

    adapter = PaymentAdapter(new_system)
    adapter.make_payment(100)
