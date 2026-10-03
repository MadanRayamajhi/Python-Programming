# Dictionaries in Python

# Creating a dictionary
student = {
    "name": "Madan",
    "age": 22,
    "course": "Computer Engineering",
    "cgpa": 2.6
}

print("Student:", student)


# Accessing values
print("\nName:", student["name"])
print("Course:", student["course"])


# Using get()
print("Age:", student.get("age"))


# Adding a new key-value pair
student["city"] = "Kathmandu"

print("\nAfter adding city:", student)


# Updating a value
student["cgpa"] = 2.8

print("After updating CGPA:", student)


# Removing an item
student.pop("city")

print("After removing city:", student)


# Dictionary keys
print("\nKeys:")
for key in student.keys():
    print(key)


# Dictionary values
print("\nValues:")
for value in student.values():
    print(value)


# Key-value pairs
print("\nStudent Information:")

for key, value in student.items():
    print(f"{key}: {value}")


# Checking if a key exists
if "name" in student:
    print("\nName exists in the dictionary.")


# Nested dictionary
students = {
    "student1": {
        "name": "Madan",
        "age": 22
    },
    "student2": {
        "name": "Ram",
        "age": 21
    }
}

print("\nNested Dictionary:")
print(students)

print("\nStudent 1 Name:", students["student1"]["name"])