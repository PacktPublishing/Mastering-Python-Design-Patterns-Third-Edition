class PaymentMethod:
    def process_payment(self, amount):
        pass


class CreditCard(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment for {amount}")


class PayPal(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment for {amount}")


print("- Choose the amount to pay")
amount = input("Enter the amount: ")
print("- Choose your payment method")
payment_method = input("Enter 'CC' for Credit Card or 'PP' for PayPal: ")

if payment_method.lower() == 'cc':
    CreditCard().process_payment(amount)
elif payment_method.lower() == 'pp':
    PayPal().process_payment(amount)
else:
    print("Invalid response")
