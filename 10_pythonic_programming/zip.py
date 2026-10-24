
# Using zip()

names = ["Ram", "Sita", "Hari"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Convert zipped values into a list
students = list(zip(names, scores))

print("\nStudent records:")
print(students)

# zip() stops at the shortest iterable by default
