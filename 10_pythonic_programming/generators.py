
# Understanding generators

def generate_numbers(limit):
    for number in range(1, limit + 1):
        yield number


# Create a generator
numbers = generate_numbers(5)

print("Generated numbers:")

for number in numbers:
    print(number)


# Generator expression
squares = (number ** 2 for number in range(1, 6))

print("\nSquares:")

for square in squares:
    print(square)
