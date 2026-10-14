
# Polymorphism in Python

class Dog:
    def sound(self):
        print("Dog barks.")

class Cat:
    def sound(self):
        print("Cat meows.")

class Cow:
    def sound(self):
        print("Cow moos.")

# Different objects, same method name
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
