class PaymentMethod:
    def __init__(self, amount: int):
        self.amount = amount

    def process_payment(self):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self):
        msg = f"Credit card payment: {self.amount}"
        print(msg)


class PayPal(PaymentMethod):
    def process_payment(self):
        msg = f"PayPal payment: {self.amount}"
        print(msg)


if __name__ == "__main__":
    test_values = [(25, "cc"), (15, "pp")]
    for amount, payment_method in test_values:
        if payment_method == "cc":
            CreditCard(amount).process_payment()
        elif payment_method == "pp":
            PayPal(amount).process_payment()
