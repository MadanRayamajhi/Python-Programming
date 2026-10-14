
# Instance Methods in Python

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Invalid amount or insufficient balance.")

    def display_balance(self):
        print("Account holder:", self.owner)
        print("Balance:", self.balance)

account = BankAccount("Madan", 5000)

account.display_balance()
account.deposit(2000)
account.withdraw(1500)
account.display_balance()
