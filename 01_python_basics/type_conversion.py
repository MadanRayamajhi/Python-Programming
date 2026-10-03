"""
Python Basics - Type Conversion
-------------------------------
Demonstrates converting values from
one data type to another.
"""

# String to integer
age_text = "22"
age = int(age_text)

print("String:", age_text)
print("Converted integer:", age)
print("Type:", type(age))

# String to float
price_text = "99.99"
price = float(price_text)

print("\nString:", price_text)
print("Converted float:", price)
print("Type:", type(price))

# Integer to float
number = 10
decimal_number = float(number)

print("\nInteger:", number)
print("Converted float:", decimal_number)

# Float to integer
value = 15.75
whole_number = int(value)

print("\nFloat:", value)
print("Converted integer:", whole_number)

# Integer to string
number = 100
number_text = str(number)

print("\nInteger:", number)
print("Converted string:", number_text)
print("Type:", type(number_text))

# List to tuple
numbers_list = [1, 2, 3, 4]
numbers_tuple = tuple(numbers_list)

print("\nList:", numbers_list)
print("Tuple:", numbers_tuple)

# Tuple to list
numbers_tuple = (5, 6, 7, 8)
numbers_list = list(numbers_tuple)

print("\nTuple:", numbers_tuple)
print("List:", numbers_list)

# String to list
text = "Python"
characters = list(text)

print("\nString:", text)
print("List:", characters)

# Boolean conversion
print("\nBoolean conversions:")
print(bool(1))
print(bool(0))
print(bool(""))
print(bool("Python"))