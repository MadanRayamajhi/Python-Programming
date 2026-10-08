
"""
Python Control Flow - Nested Conditions
"""

# Example 1: Login validation
username = "madan"
password = "python123"

if username == "madan":
    if password == "python123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# Example 2: Voting eligibility
age = int(input("Enter your age: "))
citizenship = input("Are you a Nepali citizen? (yes/no): ").lower()

if age >= 18:
    if citizenship == "yes":
        print("You meet the basic age and citizenship requirements.")
    else:
        print("Citizenship requirement is not met.")
else:
    print("You are not old enough to vote.")

# Example 3: Number classification
number = int(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
