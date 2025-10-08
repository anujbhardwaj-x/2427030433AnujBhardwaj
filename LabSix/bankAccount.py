class BankAccount:
 
    def __init__(self, acc_no, name, balance):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"rs{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance! Withdrawal failed.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        else:
            self.balance -= amount
            print(f"rs{amount} withdrawn successfully.")

    def bankFees(self):
        fees = self.balance * 0.05
        self.balance -= fees
        print(f"Bank fee of rs{fees:.2f} applied.")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account No: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance:.2f}")
        print("-----------------------")

    ac1 = BankAccount("123456", "Anuj Bhardwaj", 10000)
    ac1.display()
    ac1.deposit(5000)
    ac1.withdrawal(2000)
    ac1.bankFees()
    ac1.display()
