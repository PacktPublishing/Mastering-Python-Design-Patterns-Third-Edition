class PaymentMethod:
    def process_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment for {amount}")


class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment for {amount}")


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
