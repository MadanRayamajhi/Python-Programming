
# Handling errors using try and except

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
