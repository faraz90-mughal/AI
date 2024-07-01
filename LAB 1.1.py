# Comments in Python are marked with a hash symbol (#)

# Simple print statement
print("----Simple print statement function----\nProgramming makes life easy!!!\n")

# Input and output
print("----input/output function use----")
txt = input("Enter any String: ")
print(txt)

# Indentation and if condition
x = 1
if x > 0:
    print("----Use of indentation----\nWith if condition")

# Data types
print("\n----Different Data Types----")
a = 12
print(f"{a} is of type {type(a)}")
b = -12
print(f"{b} is of type {type(b)}")
c = 2.2
print(f"{c} is of type {type(c)}")
d = -2.2
print(f"{d} is of type {type(d)}")
st = "Strings"
print(f"{st} is of type {type(st)}")
com = complex(7, 7)
print(f"{com} is of type {type(com)}")
bol = True
print(f"{bol} is of type {type(bol)}")

# Special characters
print("\n---Special Characters or Escape Sequence---")
print("\\ symbol represents backslash.")
print("\'\t\' symbol represents tab")
print("\'Python is interpretable language.\' represents single quote.")
print("\"Python is interpretable language.\" represents double quote.")

# String access via indices
print("\n----String Access via indices----")
s = "Simplicity is the only beauty."
print(s)
num = int(input(f"Enter a number between 1 and {len(s)} to display a character from the string: "))
print(f"Requested character: {s[num-1]}")

# Slicing and methods in string
print("\n----Slicing and Methods in String----")
sli_s = s[1:7]
print(sli_s)
print(s.replace('the', 'a'))
print(s.upper())
print(s.startswith("S"))

# List data structure
print("\n----List in Python----")
lang = ['csharp', 'dart', 'kotlin', 'java']
print(lang)
number = [2, 4, 6, 8, 10]
print(number)
mix = ['app', 7, 2.2]
print(mix)

# Slicing in list
print("\n----Slicing in List----")
sli_num = number[1:4]
print(sli_num)

# Arithmetic operators
print("\n----Arithmetic Operators----")
num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} ^ {num2} = {num1 ** num2}")
print(f"{num1} % {num2} = {num1 % num2}")

# Conditional operators and if-else conditions
print("\n----Conditional Operators----")
num1 = int(input("Enter your age: "))
if num1 % 2 == 0 and num1 < 18:
    print(f"{num1} is even and under 18")
elif num1 % 2 != 0 and num1 < 18:
    print(f"{num1} is odd and under 18")
elif num1 % 2 == 0 and num1 > 18:
    print(f"{num1} is even and above 18")
elif num1 % 2 != 0 and num1 > 18:
    print(f"{num1} is odd and above 18")
else:
    print(f"{num1} is even and equal to 18")

# Comparison operators
print("\n----Comparison operators----")
month = int(input("Enter your birthday month: "))
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Entered wrong month!!!")

# >= operator with if-else conditions
marks = int(input("Enter your Marks in AI: "))
if marks >= 85:
    print("Your Grade is A+")
elif marks >= 80:
    print("Your Grade is A")
elif marks >= 75:
    print("Your Grade is B+")
elif marks >= 71:
    print("Your Grade is B")
elif marks >= 68:
    print("Your Grade is B-")
elif marks >= 64:
    print("Your Grade is C+")
elif marks >= 61:
    print("Your Grade is C")
elif marks >= 58:
    print("Your Grade is C-")
elif marks >= 54:
    print("Your Grade is D+")
elif marks >= 50:
    print("Your Grade is D")
else:
    print("Your Grade is F")
