# Tuples in Python

# Creating a tuple
coordinates = (27.7172, 85.3240)

print("Coordinates:", coordinates)

# Accessing elements
print("Latitude:", coordinates[0])
print("Longitude:", coordinates[1])


# Tuple with different data types
student = ("Madan", 22, "Computer Engineering", 2.6)

print("\nStudent:", student)


# Tuple unpacking
name, age, course, cgpa = student

print("\nName:", name)
print("Age:", age)
print("Course:", course)
print("CGPA:", cgpa)


# Tuple methods
numbers = (10, 20, 10, 30, 10, 40)

print("\nNumbers:", numbers)
print("Count of 10:", numbers.count(10))
print("Index of 30:", numbers.index(30))


# Tuple slicing
print("First three values:", numbers[:3])


# Nested tuple
student_data = (
    ("Madan", 22),
    ("Ram", 21),
    ("Sita", 23)
)

print("\nStudent Data:")

for student in student_data:
    print(student)