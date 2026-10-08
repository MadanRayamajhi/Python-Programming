
"""
Python Control Flow - While Loops
"""

# Basic while loop
count = 1

while count <= 5:
    print(count)
    count += 1

# Countdown
print("\nCountdown:")

countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Start!")

# Calculate the sum of numbers
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("\nSum from 1 to 10:", total)

# User input validation
user_number = int(input("\nEnter a positive number: "))

while user_number <= 0:
    print("Invalid input. Try again.")
    user_number = int(input("Enter a positive number: "))

print("You entered:", user_number)

# Reverse a countdown using a condition
value = 3

while value > 0:
    print("Value:", value)
    value -= 1
else:
    print("Loop completed.")
