
# Constructors in Python

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

# Create an object with initial values
student1 = Student("Madan", 22, "Computer Engineering")

student1.display()
