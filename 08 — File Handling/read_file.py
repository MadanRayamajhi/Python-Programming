
# File Handling: Reading Files

# Create a sample file for demonstration
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!\n")
    file.write("I am learning file handling.\n")
    file.write("This is my third line.")

# Example 1: Read the entire file
with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Complete file:")
    print(content)

# Example 2: Read only the first line
with open("sample.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()
    print("\nFirst line:", first_line.strip())

# Example 3: Read all lines into a list
with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print("\nAll lines:", lines)

# Example 4: Read line by line
print("\nReading line by line:")
with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
