
"""
Python Control Flow - For Loops
"""

# Loop through a range
print("Numbers from 1 to 5:")

for number in range(1, 6):
    print(number)

# Loop through a list
languages = ["Python", "Java", "C++", "JavaScript"]

print("\nProgramming Languages:")

for language in languages:
    print(language)

# Calculate the sum of numbers
total = 0

for number in range(1, 11):
    total += number

print("\nSum from 1 to 10:", total)

# Multiplication table
number = 5

print(f"\nMultiplication table of {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Nested for loops
print("\nNumber pattern:")

for row in range(1, 5):
    for column in range(row):
        print("*", end=" ")
    print()

# Loop through a string
word = "Python"

print("\nCharacters:")

for character in word:
    print(character)
