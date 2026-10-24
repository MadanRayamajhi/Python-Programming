
# Using the finally block

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    print("Error: Invalid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Program execution completed.")
