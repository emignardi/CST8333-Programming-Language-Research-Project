import os

# Read
f = open("names.txt", "r")

print(f.read())
print(f.read(7))
print(f.readline())
print(f.readline())
for line in f:
    print(line)

f.close()

try:
    f = open("names.txt", "r")
except:
    print("The file doesn't exist")
finally:
    f.close()

with open("names.txt") as f:
    content = f.read()




# Append
f = open("names.txt", "a")
f.write("\nSilly")
f.close()

f = open("names.txt", "r")
print(f.read())
f.close()




# Write (overwrite)
f = open("context.txt", "w")
f.write("Where is the text?")
f.close()

f = open("context.txt", "r")
print(f.read())
f.close()




# Create
f = open("new_file.txt", "w")
f.close()

if not os.path.exists("eric.txt"):
    f = open("eric.txt", "x")




# Delete
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
else:
    print("The file you wish to delete does not exist.")