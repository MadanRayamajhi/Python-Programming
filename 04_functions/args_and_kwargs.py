
"""
Python Functions - *args and **kwargs
Learn how to accept flexible arguments.
"""


# *args: accepts multiple positional arguments
def add_numbers(*args):
    print("Arguments:", args)
    print("Sum:", sum(args))


add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5)


# *args with a loop
def display_skills(*skills):
    print("\nSkills:")

    for skill in skills:
        print("-", skill)


display_skills("Python", "Django", "Docker", "Linux")


# **kwargs: accepts multiple keyword arguments
def display_profile(**kwargs):
    print("\nProfile:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_profile(
    name="Madan",
    profession="Developer",
    location="Nepal",
)


# Combining normal parameters, *args, and **kwargs
def student_info(name, *subjects, **details):
    print(f"\nStudent: {name}")
    print("Subjects:", subjects)
    print("Additional details:", details)


student_info(
    "Madan",
    "Python",
    "Data Science",
    "Machine Learning",
    age=22,
    university="Nepal Engineering College",
)


# Unpacking a list into positional arguments
def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]
print("\nProduct:", multiply(*numbers))


# Unpacking a dictionary into keyword arguments
def introduce(name, profession):
    print(f"{name} is a {profession}.")


person = {
    "name": "Madan",
    "profession": "Python Developer",
}

introduce(**person)
