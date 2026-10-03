# Strings in Python

name = "Madan Rayamajhi"

print("Name:", name)

# String length
print("Length:", len(name))

# Accessing characters
print("First character:", name[0])
print("Last character:", name[-1])

# String slicing
print("First five characters:", name[:5])
print("Last five characters:", name[-5:])


# String methods
message = "python programming"

print("\nOriginal:", message)
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())
print("Capitalized:", message.capitalize())


# Removing spaces
text = "   Hello Python   "

print("\nOriginal:", repr(text))
print("Stripped:", repr(text.strip()))


# Replacing text
sentence = "I am learning Java"

updated_sentence = sentence.replace("Java", "Python")

print("\nOriginal:", sentence)
print("Updated:", updated_sentence)


# Checking strings
email = "madan@example.com"

print("\nContains '@':", "@" in email)
print("Starts with 'madan':", email.startswith("madan"))
print("Ends with '.com':", email.endswith(".com"))


# f-string
name = "Madan"
age = 22

print(f"\nMy name is {name} and I am {age} years old.")