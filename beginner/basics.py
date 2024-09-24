# Paradigms: Procedural, Object-Oriented & Functional

# Modules
import sys # System-spefic Parameters and Functions Module
import random # Random Module
print(sys.version) # Python Version

# Command Line Commands & Read Eval Print Loop (REPL)
# python
# exit()

# Console Output
print("Hello World") # Console Output

# User Input
userInput = input("What is your favourite instrument?")

# Variables & Data Types
name = "Eric" # String
lastName = str(" Mignardi ") # String Constructor
slicedName = name[2:4] # String Slice
lowercase = name.lower()
uppercase = name.upper()
strip = lastName.strip()
replace = name.replace("c", "e")
a = "Hello, World!"
b = a.split(",")
c = f"Hello {name}" # F-String
price = 59
txt = f"The price is {price:.2f} dollars"
multiline = """this
is an odd format
for a multiline string"""
age = 28 # Integer
catAge = int(10) # Integer Constructor
patience = 10.9 # Float
x = 35e3 # Float
y = 12E4 # Float
z = -87.7e100 # Float
number0 = 1j # Complex
random = random.randrange(1, 10) # Random Range (1-9)
countdown = range(10) # Range (0-9)
for num in countdown: # Range Test
    print(num)
single = True # Boolean
Single = False # Case Sensitivity
boolean = bool("Hello") # True
number = int(10.5) # Casting
print(type(number))

# Access Modifiers - Access To Data Inside/Outside Of Class
varPublic = 65 # Accessible Both Inside/Outside of Class
_varProtected = 65 # Accessible Inside Class And Its Subclass
__varPrivate = 65 # Accessible Only Inside Class

# Data Structures
friends = ["Tadoe", "Bubs", "Leon"] # List (ordered, mutable, duplicates)
tadoe = friends[0]
friends.append("Food")
friends.remove("Leon")
friends.pop(1)
friendsCopy = friends.copy
len(friends)
type(friends)
languages = {"Java" : 1, "Python" : 2, "JavaScript" : 3} # Dictionary (ordered*, mutable, no duplicates)
one = languages["Java"]
two = languages.get("Python")
keys = languages.keys()
values = languages.values()
items = languages.items()
languages["JavaScript"] = 100
languages["C"] = 4
languages.update({"C#" : 5})
food = {"Burger", "Pizza", "Candy"} # Set (unordered, immutable but can add/remove, unindexed, no duplicates)
parents = ("Norma", "John") # Tuple (ordered, immutable, duplicates)
john = parents[1]
friends.extend(parents)
fruits = ["banana", "strawberry", "peach"] # Unpacking Collection
a, b, c = fruits
print(a + b + c)

# Scope (Global & Local)
globalVar = "Eric"
def testScope():
    globalVar = "Mignardi"
    print(globalVar)
testScope()
print(globalVar)

def testScope2():
    global globalVar
    globalVar = "Mignardi"
    print(globalVar)
testScope2()
print(globalVar)

# Operators
l = 1 + 2 # Arithmetic Operators
m = 4 * 2
n = 4 / 2
o = 4 ** 4
p = 4 // 4
# Logical Operators (and, or, not)
# Identity Operators (is, is not)
# Membership Operators (in, not in)
# Bitwise Operators (&, |, ^, ~)

# Conditionals
if l > m:
    print("L is greater")
elif l == m:
    print("L is equal")
else:
    print("L is less than")

print("L is greater") if l > m else print("L is not greater")

# Loops
i = 1
while i < 6:
    print(i)
    i += 1

for fruit in fruits:
    print(fruit)

for number99 in range(6):
    print(number99)

# Functions
def my_function(myName):
    print("this is a function" + myName)
my_function("Eric")

# Lambdas
squared = lambda num : num * num # Lambda
print(squared(2))

addition = lambda a, b : a + b # Lambda (Two Parameters)
print(addition(100, 100))

# addTwo = lambda num : num + 2
def addTwo(num): return num + 2 # Lambda Formatted As Function
print(addTwo(12))

# Higher Order Function (Takes one or more functions as arguments or returns a function as result)
def funcBuilder(x):
    return lambda num : num + x
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)
print(addTen(86))
print(addTwenty(76))

# Classes & Objects
class User: # Class
    def __init__(self, name, age): # Constructor
        self.name = name
        self.age = age
    def __str__(self): # toString
        return f"{self.name} is {self.age} years old."
    def myFunction(self):
        print("Hello " + self.name)

user = User("Eric", 28) #Object
user.myFunction()
print(user)

class Child(User): # Inheritance
    def myFunction(self): # Method Overriding & Polymorphism
        print("Hello from Child " + self.name)
child = Child("Tadoe", 10)
class Adult(User):
    def myFunction(self):
        print("Hello from Adult " + self.name)
adult = Adult("John", 64)
child.myFunction()
adult.myFunction()

# Closures
def parent_function(person, coins): # Closures
    # coins = 3
    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print(person + " has " + str(coins) + " coins left")
        elif coins == 1:
            print(person + " has " + str(coins) + " coin left")
        else:
            print(person + " has " + str(coins) + " is out of coins")
    return play_game
tommy = parent_function("Tommy", 3)
jenny = parent_function("Jenny", 3)
tommy()
tommy()
jenny()

# Exceptions
notHere = 2

class CustomError(Exception): # Custom Exception
    pass

try: # Try-Except-Finally Block
    raise CustomError("This is a custom error") # Raising Error
    # raise Exception("I'm a custom exception")
    # print(notHere / 0)
    # if not type(notHere) is str:
    #     raise TypeError("only strings are allowed")
except ZeroDivisionError as e:
    print(e)
else:
    print("There is no error")
finally:
    print("I'm going to print with or without error")

# Comprehensions
doubles = []
for x in range(1, 10):
    doubles.append(x * 2)

doubles_comp = [x * 2 for x in range(1, 10)]