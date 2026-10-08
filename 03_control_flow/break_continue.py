
"""
Python Control Flow - Break and Continue
"""

# Example 1: break
# Stop the loop when the number reaches 5

print("Break example:")

for number in range(1, 11):
    if number == 5:
        break

    print(number)

# Example 2: continue
# Skip the number 5

print("\nContinue example:")

for number in range(1, 11):
    if number == 5:
        continue

    print(number)

# Example 3: Find the first matching number
print("\nFinding a number:")

numbers = [3, 7, 12, 18, 25]

for number in numbers:
    if number > 10:
        print("First number greater than 10:", number)
        break

# Example 4: Skip even numbers
print("\nOdd numbers from 1 to 10:")

for number in range(1, 11):
    if number % 2 == 0:
        continue

    print(number)

# Example 5: Break in a while loop
print("\nWhile loop with break:")

count = 1

while count <= 10:
    if count == 6:
        break

    print(count)
    count += 1

print("Loop stopped.")
