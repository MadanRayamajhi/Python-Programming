
# Using map(), filter(), and reduce()

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map(): Square every number
squares = list(map(lambda number: number ** 2, numbers))
print("Squares:", squares)

# filter(): Select even numbers
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)
print("Even numbers:", even_numbers)

# reduce(): Calculate the sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# Another example: Multiply all numbers
product = reduce(lambda x, y: x * y, numbers)
print("Product:", product)
