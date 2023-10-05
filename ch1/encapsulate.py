class PaymentMethod:
    def process_payment(self, amount: int):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self, amount: int):
        msg = f"Processing credit card payment: {amount}"
        print(msg)


class PayPal(PaymentMethod):
    def process_payment(self, amount: int):
        msg = f"Processing PayPal payment: {amount}"
        print(msg)


if __name__ == "__main__":
    print("- Choose the amount to pay")
    msg = "Which amount? "
    amount = input(msg)
    print("- Choose your payment method")
    msg = "'CC' for Credit Card or 'PP' for PayPal: "
    payment_method = input(msg)

    if payment_method.lower() == 'cc':
        CreditCard().process_payment(amount)
    elif payment_method.lower() == 'pp':
        PayPal().process_payment(amount)
    else:
        print("Invalid response")
