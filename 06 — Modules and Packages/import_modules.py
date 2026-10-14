
# Import Modules in Python

# Import the complete math module
import math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))

# Import a specific function
from random import randint

print("Random number:", randint(1, 10))

# Import a module with an alias
import statistics as stats

numbers = [10, 20, 30, 40, 50]

print("Mean:", stats.mean(numbers))
print("Median:", stats.median(numbers))

# Import multiple functions
from math import factorial, ceil

print("Factorial:", factorial(5))
print("Ceiling:", ceil(4.3))
