
# File Handling: Writing Files

# Example 1: Write text to a file
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("This file was created using Python.\n")
    file.write("Writing files is easy.")

print("Data written successfully.")

# Example 2: Write multiple lines
lines = [
    "Python\n",
    "Java\n",
    "C++\n",
    "JavaScript\n"
]

with open("languages.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print("Programming languages saved successfully.")

# Example 3: Read the saved content
with open("notes.txt", "r", encoding="utf-8") as file:
    print("\nSaved content:")
    print(file.read())
