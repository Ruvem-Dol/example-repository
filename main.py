# Basic overview of Python syntax:

# 1. Printing to the console:
print("Hello, World!")

# 2. Variables and Data Types:
x = 5          # Integer
y = 3.14       # Float
name = "Alice" # String
is_active = True # Boolean

# 3. Lists:
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

# 4. Tuples:
coordinates = (10, 20)
print(coordinates[1])  # Output: 20

# 5. Dictionaries:
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice

# 6. Conditional Statements:
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# 7. Loops:
# For loop
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# 8. Functions:
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# 9. Classes:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

alice = Person("Alice", 25)
print(alice.greet())  # Output: Hello, my name is Alice and I am 25 years old.

# The code below is a basic overview of Python syntax, including examples of printing to the console, 
# variables and data types, lists, tuples, dictionaries, conditional statements, loops, functions, and classes.
# This should cover the basics to get you started with Python again!
