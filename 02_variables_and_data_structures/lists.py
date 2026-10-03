# Lists in Python

# Creating a list
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# Adding an element
fruits.append("Grapes")

print("\nAfter append:", fruits)


# Inserting an element
fruits.insert(1, "Watermelon")

print("After insert:", fruits)


# Removing an element
fruits.remove("Banana")

print("After remove:", fruits)


# Updating an element
fruits[0] = "Pineapple"

print("After update:", fruits)


# List slicing
print("\nFirst three fruits:", fruits[:3])


# List length
print("Number of fruits:", len(fruits))


# Sorting
numbers = [45, 12, 89, 23, 5]

print("\nOriginal numbers:", numbers)

numbers.sort()

print("Sorted numbers:", numbers)


# Reverse
numbers.reverse()

print("Reversed numbers:", numbers)


# Loop through a list
print("\nFruits:")
for fruit in fruits:
    print("-", fruit)