
# Creating a custom exception

class InsufficientBalanceError(Exception):
    """Raised when the account has insufficient balance."""
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Withdrawal amount must be positive.")

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance for withdrawal."
        )

    balance -= amount
    return balance


try:
    balance = 5000
    amount = float(input("Enter withdrawal amount: "))

    remaining_balance = withdraw(balance, amount)

    print("Withdrawal successful.")
    print("Remaining balance:", remaining_balance)

except ValueError as error:
    print("Invalid input:", error)

except InsufficientBalanceError as error:
    print("Transaction failed:", error)
