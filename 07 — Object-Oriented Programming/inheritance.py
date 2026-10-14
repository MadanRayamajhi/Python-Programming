
# Inheritance in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print("Course:", self.course)
        print("I am studying.")


student = Student("Madan", 22, "Computer Engineering")

student.introduce()
student.study()
