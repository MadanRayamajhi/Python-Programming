"""
Python Basics - Operators
-------------------------
Demonstrates arithmetic, comparison,
logical, assignment, membership,
identity, and bitwise operators.
"""

# ---------------------------------
# 1. Arithmetic Operators
# ---------------------------------

a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)


# ---------------------------------
# 2. Comparison Operators
# ---------------------------------

x = 10
y = 20

print("\nComparison Operators")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# ---------------------------------
# 3. Logical Operators
# ---------------------------------

age = 22
has_id = True

print("\nLogical Operators")
print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)


# ---------------------------------
# 4. Assignment Operators
# ---------------------------------

number = 10

number += 5
print("\nAfter += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 4
print("After /= :", number)


# ---------------------------------
# 5. Membership Operators
# ---------------------------------

languages = ["Python", "Java", "C++"]

print("\nMembership Operators")
print("Python" in languages)
print("PHP" not in languages)


# ---------------------------------
# 6. Identity Operators
# ---------------------------------

list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print("\nIdentity Operators")
print("list_a is list_b:", list_a is list_b)
print("list_a is list_c:", list_a is list_c)
print("list_a == list_c:", list_a == list_c)


# ---------------------------------
# 7. Bitwise Operators
# ---------------------------------

a = 5
b = 3

print("\nBitwise Operators")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)