# Paradigms: Procedural, Object-Oriented & Functional

import sys # System-spefic Parameters and Functions Module
import random # Random Module
print(sys.version) # Python Version
print("Hello World") # Console Output

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



# Python Command Line Commands & Read Eval Print Loop (REPL)
# python
# exit()



fruits = ["banana", "strawberry", "peach"] # Unpacking Collection
a, b, c = fruits
print(a + b + c)



globalVar = "Eric" # Global & Local Scope
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



l = 1 + 2 # Arithmetic Operators
m = 4 * 2
n = 4 / 2
o = 4 ** 4
p = 4 // 4
# Logical Operators (and, or, not)
# Identity Operators (is, is not)
# Membership Operators (in, not in)
# Bitwise Operators (&, |, ^, ~)



if l > m: # Conditionals
    print("L is greater")
elif l == m:
    print("L is equal")
else:
    print("L is less than")

print("L is greater") if l > m else print("L is not greater")



i = 1 # Loops
while i < 6:
    print(i)
    i += 1

for fruit in fruits:
    print(fruit)

for number99 in range(6):
    print(number99)



def my_function(myName): # Functions
    print("this is a function" + myName)

my_function("Eric")



class User: # Class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    def myFunction(self):
        print("Hello " + self.name)

user = User("Eric", 28) #Object
user.myFunction()

print(user)