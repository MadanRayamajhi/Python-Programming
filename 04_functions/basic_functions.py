
"""
Python Functions - Basic Functions
Learn how to define and call functions.
"""


# Function without parameters
def greet():
    print("Hello, Python!")
    print("Welcome to function programming.")


greet()


# Function with one parameter
def greet_user(name):
    print(f"Hello, {name}!")


greet_user("Madan")
greet_user("Ram")


# Function with multiple parameters
def introduce(name, age, profession):
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I work as a {profession}.")


introduce("Madan", 22, "Developer")


# Function to display a separator
def print_separator():
    print("-" * 30)


print_separator()
print("Python Learning")
print_separator()


# Function with a default parameter
def welcome(name="Guest"):
    print(f"Welcome, {name}!")


welcome()
welcome("Madan")


# Main entry point
if __name__ == "__main__":
    print("\nProgram executed successfully.")
