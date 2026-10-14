
# File Handling: Appending Files

# Create an initial file
with open("activity.txt", "w", encoding="utf-8") as file:
    file.write("Day 1: Learned Python basics.\n")

print("Initial content created.")

# Example 1: Append a new line
with open("activity.txt", "a", encoding="utf-8") as file:
    file.write("Day 2: Learned loops.\n")

print("New content appended.")

# Example 2: Append another line
with open("activity.txt", "a", encoding="utf-8") as file:
    file.write("Day 3: Learned file handling.\n")

print("Another line appended.")

# Example 3: Display the complete file
with open("activity.txt", "r", encoding="utf-8") as file:
    print("\nComplete activity log:")
    print(file.read())
