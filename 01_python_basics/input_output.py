"""
Python Basics - Input and Output
--------------------------------
Demonstrates how to take user input
and display formatted output.
"""

# Basic input
name = input("Enter your name: ")

print("Hello,", name)

# Input is always received as a string
age = input("Enter your age: ")

print("Your age is:", age)
print("Data type of age:", type(age))

# Converting input to integer
age = int(input("Enter your age again: "))

print(f"You are {age} years old.")

# Taking multiple inputs
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Full Name: {first_name} {last_name}")

# Taking numeric input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")

# Formatted output
student = "Madan"
marks = 85

print(f"Student: {student}")
print(f"Marks: {marks}%")