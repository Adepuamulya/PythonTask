#Payment System (Runtime Polymorphism) 
#An online store supports multiple payment methods: CreditCard, UPI, and NetBanking. Create a base class Payment with a method process_payment() and override it in each payment type. 
class Payment:
    def process_payment(self, amount):
        print("Processing payment of", amount)

class CreditCard(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "processed using Credit Card")

class UPI(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "processed using UPI")

class NetBanking(Payment):
    def process_payment(self, amount):
        print("Payment of", amount, "processed using Net Banking")

amount = float(input("Enter payment amount: "))
method = input("Choose payment method (credit/upi/netbanking): ").lower()

if method == "credit":
    payment = CreditCard()
elif method == "upi":
    payment = UPI()
elif method == "netbanking":
    payment = NetBanking()
else:
    print("Invalid payment method")
    payment = Payment()

payment.process_payment(amount)