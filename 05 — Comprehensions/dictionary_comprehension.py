
# Dictionary Comprehension in Python

# Example 1: Create a dictionary of squares
squares = {number: number ** 2 for number in range(1, 6)}

print("Squares dictionary:", squares)

# Example 2: Create a dictionary from two lists
names = ["Madan", "Ram", "Sita"]
ages = [22, 23, 21]

people = {name: age for name, age in zip(names, ages)}

print("People:", people)

# Example 3: Filter dictionary values
marks = {
    "Madan": 85,
    "Ram": 45,
    "Sita": 92,
    "Hari": 38
}

passed_students = {
    name: mark for name, mark in marks.items() if mark >= 40
}

print("Passed students:", passed_students)

# Example 4: Convert values to uppercase
languages = {
    "first": "python",
    "second": "java",
    "third": "c++"
}

uppercase_languages = {
    key: value.upper() for key, value in languages.items()
}

print("Languages:", uppercase_languages)
