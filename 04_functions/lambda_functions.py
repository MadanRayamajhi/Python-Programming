
"""
Python Functions - Lambda Functions
Learn small anonymous functions and common use cases.
"""


# Basic lambda function
square = lambda number: number ** 2

print("Square:", square(5))


# Lambda with multiple arguments
add = lambda a, b: a + b

print("Sum:", add(10, 20))


# Lambda with a conditional expression
check_number = lambda number: (
    "Even" if number % 2 == 0 else "Odd"
)

print("Number 8:", check_number(8))
print("Number 7:", check_number(7))


# Sorting using a lambda function
students = [
    {"name": "Ram", "marks": 75},
    {"name": "Madan", "marks": 90},
    {"name": "Sita", "marks": 85},
]

students_sorted = sorted(
    students,
    key=lambda student: student["marks"],
    reverse=True,
)

print("\nStudents sorted by marks:")

for student in students_sorted:
    print(student["name"], student["marks"])


# Using lambda with map()
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number ** 2, numbers))

print("\nSquares:", squares)


# Using lambda with filter()
even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)


# Prefer a normal def for complex logic.
def calculate_cube(number):
    return number ** 3


print("Cube:", calculate_cube(3))
