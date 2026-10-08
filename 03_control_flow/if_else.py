
"""
Python Control Flow - If, Elif, Else
"""

# Basic if statement
age = 22

if age >= 18:
    print("You are an adult.")

# If-else statement
number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# If-elif-else statement
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Needs Improvement"

print("Marks:", marks)
print("Grade:", grade)

# User input example
temperature = float(input("Enter temperature in Celsius: "))

if temperature > 30:
    print("The weather is hot.")
elif temperature >= 15:
    print("The weather is moderate.")
else:
    print("The weather is cold.")
