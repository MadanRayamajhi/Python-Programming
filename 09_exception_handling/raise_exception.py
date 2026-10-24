
# Raising an exception manually

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

elif age < 18:
    print("You are a minor.")

else:
    print("You are an adult.")
