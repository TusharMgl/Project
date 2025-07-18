from datetime import datetime
import uuid

class PaymentSystem:
    def __init__(self):
        self.current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def process_payment(self):
        try:
            self.holder_name = input("Enter the Holder Name: ")
            self.amount = int(input("Enter the amount: "))
            self.payment_method = input("Enter the payment method (cash or online): ")
            self.transaction_id = int(uuid.uuid4())

        except ValueError:
            print("Please enter a valid amount.")

    def generate_receipt(self):
        receipt_template = """
        Payment Receipt
        ----------------
        Date: {}
        Amount: ${}
        Transaction ID: {}
        Holder Name: {}
        Payment Method: {}
        ----------------
        Thank you for your payment!
        """
        return receipt_template.format(self.current_date_time, self.amount, self.transaction_id,
                                       self.holder_name, self.payment_method)

    def save_receipt_to_file(self, receipt, filename):
        try:
            with open("Tushar.txt", 'w') as file:
                file.write(receipt)
            print(f"Receipt saved to {filename}")
        except Exception as e:
            print(f"Error occurred while saving receipt: {str(e)}")


def main():
    payment_system = PaymentSystem()
    payment_system.process_payment()
    receipt = payment_system.generate_receipt()
    print(receipt)

    filename = f"receipt_{payment_system.transaction_id}.txt"
    payment_system.save_receipt_to_file(receipt, filename)

if __name__ == "__main__":
    main()
