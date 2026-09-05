# ==========================================
# DAY-04 – TECHNICAL TRAINING
# Stack, Patterns, Strings & Python Practice
# ==========================================


# ==========================================
# 1. CONSTRUCTOR
# ==========================================

class Student:

    def __init__(self):
        print("I will be called automatically")

    def message(self):
        print("Hello inside class")


obj = Student()
obj1 = Student()

print(obj)

obj.message()


# ==========================================
# 2. STACK USING LIST
# ==========================================

import sys


class Stack:

    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.stacklist = []

    # Check whether stack is full
    def isfull(self):
        if len(self.stacklist) == self.stacksize:
            return True
        else:
            return False

    # Check whether stack is empty
    def isempty(self):
        if len(self.stacklist) == 0:
            return True
        else:
            return False

    # Add element to stack
    def push(self, data):
        if self.isfull():
            print("Stack is full")
        else:
            self.stacklist.append(data)
            print(data, "pushed into stack")

    # Remove top element
    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Popped element:", self.stacklist.pop())

    # Display top element
    def peek(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Top element:", self.stacklist[-1])

    # Delete stack
    def deletestack(self):
        if self.isempty():
            print("Stack is empty")
        else:
            self.stacklist.clear()
            print("Stack has been deleted")

    # Display stack
    def displaystack(self):
        print("Stack:", self.stacklist)


size = int(input("Enter the size of stack: "))

objstack = Stack(size)

while True:

    print("\n1. Push element")
    print("2. Pop element")
    print("3. Peek element")
    print("4. Is Empty")
    print("5. Is Full")
    print("6. Delete Stack")
    print("7. Display Stack")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to push: "))
        objstack.push(value)

    elif choice == 2:
        objstack.pop()

    elif choice == 3:
        objstack.peek()

    elif choice == 4:
        print("Stack is empty:", objstack.isempty())

    elif choice == 5:
        print("Stack is full:", objstack.isfull())

    elif choice == 6:
        objstack.deletestack()

    elif choice == 7:
        objstack.displaystack()

    elif choice == 8:
        print("Exit")
        sys.exit()

    else:
        print("Invalid input")


# ==========================================
# 3. NESTED LOOP – BASIC PATTERN
# ==========================================

for i in range(1, 4):

    for j in range(1, 4):
        print(i, end=" ")

    print()


# ==========================================
# 4. NUMBER PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):
        print(i, end=" ")

    print()


# ==========================================
# 5. ALPHABET PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):
        print(chr(64 + i), end=" ")

    print()


# ==========================================
# 6. REVERSE NUMBER PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 1):
        print(n + 1 - i, end=" ")

    print()


# ==========================================
# 7. STAR PATTERN – SAME NUMBER OF STARS
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, 2):
        print("*", end=" ")

    print()


# ==========================================
# 8. INCREASING STAR PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print("*", end=" ")

    print()


# ==========================================
# 9. INCREASING ALPHABET PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(chr(64 + i), end=" ")

    print()


# ==========================================
# 10. DECREASING ALPHABET PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 2 - i):
        print(chr(64 + i), end=" ")

    print()


# ==========================================
# 11. DECREASING ALPHABET PATTERN – A, B, C
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 2 - i):
        print(chr(64 + j), end=" ")

    print()


# ==========================================
# 12. REVERSE NUMBER PATTERN WITH DELAY
# ==========================================

import time

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    for j in range(1, n + 2 - i):
        time.sleep(2)
        print(n + 1 - i, end=" ")

    print()


# ==========================================
# 13. STAR PYRAMID
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    print(" " * (n - i), end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()


# ==========================================
# 14. ALPHABET PYRAMID
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    print(" " * (n - i), end=" ")

    for j in range(1, i + 1):
        print(chr(64 + i), end=" ")

    print()


# ==========================================
# 15. ALPHABET PYRAMID – A, B, C
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    print(" " * (n - i), end=" ")

    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")

    print()


# ==========================================
# 16. NUMBER PYRAMID PATTERN
# ==========================================

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):

    print(" " * (n - i), end=" ")

    for j in range(1, i):
        print(i - j, end=" ")

    for k in range(0, i):
        print(k, end=" ")

    print()


# ==========================================
# 17. STRING FORMATTING
# ==========================================

print("Subject marks:")

phy = 50
chem = 60
math = 70

print(
    "Physics={} Chemistry={} Math={}".format(
        phy, chem, math
    )
)

print(
    "Physics={0} Chemistry={1} Math={2}".format(
        phy, chem, math
    )
)

print(
    "Physics={x} Chemistry={y} Math={z}".format(
        x=phy,
        y=chem,
        z=math
    )
)

total = phy + chem + math

print("Total marks:", f"{total}")

print("Roll No =", "7".zfill(4))


# ==========================================
# 18. STRING CASE FUNCTIONS
# ==========================================

s = "Python is a High level programming Language"

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())


# ==========================================
# 19. JOIN FUNCTION
# ==========================================

s = ("suraj", "kumar", "mishra")

name = "-".join(s)

print(name)


# ==========================================
# 20. FIND FUNCTION
# ==========================================

s = "help4code is a best platform for practicing programming"

print(s.find("help4code"))
print(s.find("python"))
print(s.find("programming"))


# ==========================================
# 21. STRING CHECKING FUNCTIONS
# ==========================================

print("suraj48877".isalnum())
print("surajmishra".isalpha())
print("48877".isdigit())
print("bskjj".islower())
print("".islower())
print("SURAJm".isupper())
print("My Name is Suraj".istitle())
print("".istitle())
print("".isspace())
print("Hello".startswith("He"))
print("Hello".endswith("lo"))


# ==========================================
# 22. STRING SLICING
# ==========================================

name = "suraj"

print(name[0])
print(name[1])
print(name[-1])
print(name[0:4])
print(name[2:])
print(name[:4])
print(name[:])
print(name[::-1])
print(name[0:4:1])
print(name[0:4:2])


# ==========================================
# 23. TRAVERSE STRING USING for LOOP
# ==========================================

for i in "suraj":
    print(i, end=" ")

print()

for i in "suraj":
    print(i)


# ==========================================
# 24. STRING INDEXING USING range()
# ==========================================

name = "suraj"

for i in range(len(name)):
    print(name[i], end=" ")

print()


# ==========================================
# 25. REVERSE LOOP
# ==========================================

for i in range(4, 0, -1):
    print(i)


# ==========================================
# 26. REVERSE STRING USING INDEX
# ==========================================

name = "suraj"

for i in range(len(name) - 1, -1, -1):
    print(name[i], end=" ")

print()


# ==========================================
# 27. REMOVE DUPLICATE CHARACTERS
# ==========================================

name = "surajkumarmishra"

newname = ""

for i in name:

    if i not in newname:
        newname += i

print("Original Name:", name)
print("Without Duplicate Characters:", newname)
