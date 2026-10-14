
# List Comprehension in Python

# Example 1: Create a list of squares
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print("Squares:", squares)

# Example 2: Get even numbers
even_numbers = [number for number in range(1, 11) if number % 2 == 0]

print("Even numbers:", even_numbers)

# Example 3: Convert names to uppercase
names = ["madan", "ram", "sita"]
uppercase_names = [name.upper() for name in names]

print("Uppercase names:", uppercase_names)

# Example 4: Extract long words
words = ["Python", "is", "easy", "to", "learn"]
long_words = [word for word in words if len(word) > 3]

print("Long words:", long_words)

# Example 5: If-else inside list comprehension
results = ["Even" if number % 2 == 0 else "Odd"
           for number in range(1, 6)]

print("Results:", results)
