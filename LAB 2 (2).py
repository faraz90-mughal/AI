# While loop example
print("\n----while loop---")
count = 0
while count < 3:
    count += 1 
    print("Hello Geek")
print()

# While loop for printing multiplication table
num = int(input("Enter number to display table: "))
i = 1
while i <= 10:
    print(f"{i} * {num} = {i * num}")
    i += 1
print()

# For loop traversal using list
print("\n----for loop traversal using list----")
ai = ['robotics', 'deep learning', 'automation']
for item in ai:
    print(item)
print()

# For loop traversal by index of sequence
print("\n----for loop traversal by index of sequence----")
li = ['windows', 'linux', 'macOS']
for index, item in enumerate(li):
    print(index)
print()

# For loop with break statement
br = int(input("Enter number to exit loop (1 to 10): "))
for i in range(1, 11):
    print(i)
    if i == br:
        break
print()

# For loop with continue statement
con = int(input("Enter a number to display even numbers (1 to your number): "))
for i in range(1, con + 1):
    if i % 2 != 0:
        continue
    print(i)
print()

# Function examples
print("\n-----Functions-----")

# Simple function
def display():
    print("Programming makes life easy!!!")

display()

# Function with parameters and return
def sum(num1, num2):
    return num1 + num2

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"Sum of {num1} + {num2}: {sum(num1, num2)}")

# Function with default argument
name = input("Enter your name: ")
def greeting(name, greeting="have a nice day!!!"):
    print(f"{name} {greeting}")
greeting(name)
print()

# Function to find factorial
def factorial(value):
    if value < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if value == 0 or value == 1:
        return 1
    return value * factorial(value - 1)

value = int(input("Enter number for factorial: "))
print(factorial(value))

# Class examples
print("\n-----class------")

# Simple class
class AI:
    str = "Classes are parts of Object Oriented Programming."

obj = AI()
print(obj.str)

# Class with constructor (__init__ method)
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

na = input("Enter your name: ")
ag = int(input(f"Enter {na}'s age: "))
co = input(f"Enter {na}'s country name: ")
p1 = Person(na, ag, co)
print(f"{p1.name} is {p1.age} years old and lives in {p1.country}.\n")

# Class with method
class Room:
    def __init__(self):
        self.length = 0.0
        self.breadth = 0.0
    
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)

study_room = Room()
study_room.length = float(input("Enter length: "))
study_room.breadth = float(input("Enter breadth: "))
study_room.calculate_area()
