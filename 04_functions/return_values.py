
"""
Python Functions - Return Values
Learn how functions return results.
"""


# Return a single value
def square(number):
    return number ** 2


result = square(5)
print("Square:", result)


# Return the sum of two numbers
def add(a, b):
    return a + b


print("Sum:", add(10, 20))


# Return multiple values
def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


sum_result, difference, product = calculate(10, 5)

print("Addition:", sum_result)
print("Subtraction:", difference)
print("Multiplication:", product)


# Return a boolean
def is_even(number):
    return number % 2 == 0


print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))


# Return a list
def get_even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


values = [1, 2, 3, 4, 5, 6, 7, 8]
print("Even numbers:", get_even_numbers(values))


# Return None explicitly when appropriate
def check_age(age):
    if age < 0:
        return None

    return age >= 18


print("Adult:", check_age(22))
print("Invalid age:", check_age(-1))
