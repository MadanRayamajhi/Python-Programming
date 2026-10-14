
# File Handling: JSON Files

import json

# Example 1: Create Python data
student = {
    "name": "Madan",
    "age": 22,
    "course": "Computer Engineering",
    "skills": ["Python", "SQL", "Git"],
    "is_learning": True
}

# Example 2: Write Python data to a JSON file
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("JSON file created successfully.")

# Example 3: Read JSON data from a file
with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print("\nStudent information:")
print("Name:", loaded_student["name"])
print("Age:", loaded_student["age"])
print("Course:", loaded_student["course"])
print("Skills:", loaded_student["skills"])
print("Learning:", loaded_student["is_learning"])

# Example 4: Convert Python dictionary to JSON string
json_string = json.dumps(student, indent=4)

print("\nJSON string:")
print(json_string)

# Example 5: Convert JSON string to Python data
python_data = json.loads(json_string)

print("\nConverted back to Python:")
print(type(python_data).__name__)
print(python_data["name"])
