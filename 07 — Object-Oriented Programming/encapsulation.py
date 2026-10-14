
# Encapsulation in Python

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Amount must be positive.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Madan", 5000)

print("Owner:", account.owner)
print("Initial balance:", account.get_balance())

account.deposit(2000)

print("Updated balance:", account.get_balance())

# The following would raise AttributeError:
# print(account.__balance)
