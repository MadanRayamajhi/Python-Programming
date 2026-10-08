
"""
Python Functions - Parameters
Learn positional, keyword, default, and mixed arguments.
"""


# Positional arguments
def add_numbers(a, b):
    print("Sum:", a + b)


add_numbers(10, 20)


# Keyword arguments
def display_student(name, age, course):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Course: {course}")


display_student(
    name="Madan",
    age=22,
    course="Computer Engineering"
)


# Default parameters
def calculate_price(price, tax_rate=0.13):
    total = price + (price * tax_rate)
    print(f"Total price: {total:.2f}")


calculate_price(1000)
calculate_price(1000, 0.10)


# Multiple parameters
def calculate_average(a, b, c):
    average = (a + b + c) / 3
    print(f"Average: {average:.2f}")


calculate_average(80, 90, 85)


# Keyword arguments in a different order
def describe_person(name, city):
    print(f"{name} lives in {city}.")


describe_person(city="Kathmandu", name="Madan")


# Avoid mutable default arguments.
def add_skill(skill, skills=None):
    if skills is None:
        skills = []

    skills.append(skill)
    return skills


print(add_skill("Python"))
print(add_skill("Docker"))
