
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = meena
        self.account_number = account_number
        self.balance = balance

    def check_balance(self):
        print("\n----- BANK ACCOUNT DETAILS -----")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Available Balance: ₹", self.balance)

name = input("Enter acc holder name: ")
account_number = input("Enter account no ")
balance = float(input("Enter account balance: "))

account = BankAccount(name, acc_number, balance)

account.check_balance()
print("avanthi")