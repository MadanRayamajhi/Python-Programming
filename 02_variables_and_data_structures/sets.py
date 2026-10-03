# Sets in Python

# Creating a set
numbers = {10, 20, 30, 40, 50}

print("Numbers:", numbers)


# Sets automatically remove duplicates
values = {1, 2, 2, 3, 3, 4, 4}

print("\nSet with duplicates removed:", values)


# Adding an element
numbers.add(60)

print("\nAfter adding 60:", numbers)


# Adding multiple elements
numbers.update([70, 80, 90])

print("After adding multiple values:", numbers)


# Removing an element
numbers.remove(20)

print("After removing 20:", numbers)


# Discard does not raise an error if the item doesn't exist
numbers.discard(100)

print("After discard:", numbers)


# Set operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("\nSet A:", set_a)
print("Set B:", set_b)

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("A - B:", set_a - set_b)

# Symmetric difference
print("Symmetric Difference:", set_a ^ set_b)


# Membership testing
print("\nIs 3 present in Set A?", 3 in set_a)
print("Is 10 present in Set A?", 10 in set_a)