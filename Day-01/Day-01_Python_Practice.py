# ==========================================
# DAY 01 - PYTHON PRACTICE
# Technical Training Program
# ==========================================


# ------------------------------------------
# 1. Data Types & Dynamic Typing
# ------------------------------------------

math = 50          # int
chem = 60          # int
phy = 70           # int
name = "Suraj"     # str
pi = 3.14          # float

print(type(math))
print(type(chem))
print(type(phy))
print(type(name))
print(type(pi))


# ------------------------------------------
# 2. Check Address / Identity using id()
# ------------------------------------------

print(id(math))
print(id(chem))
print(id(phy))
print(id(name))
print(id(pi))


# ------------------------------------------
# 3. Reverse a 3-Digit Number
# 123 -> 321
# ------------------------------------------

num = 123

a = num % 10
num = num // 10

b = num % 10
c = num // 10

rev = a * 100 + b * 10 + c

print("Reverse:", rev)


# ------------------------------------------
# 4. Reverse a 6-Digit Number
# 123456 -> 654321
# ------------------------------------------

num = 123456

a = num % 10
num = num // 10

b = num % 10
num = num // 10

c = num % 10
num = num // 10

d = num % 10
num = num // 10

e = num % 10
num = num // 10

f = num % 10

rev = (
    a * 100000
    + b * 10000
    + c * 1000
    + d * 100
    + e * 10
    + f
)

print("Reverse:", rev)


# ------------------------------------------
# 5. Swapping Two Numbers
# Using Third Variable
# ------------------------------------------

val1 = int(input("Enter the value: "))
val2 = int(input("Enter the value: "))

print("Before Swapping:", "val1 =", val1, "val2 =", val2)

temp = val1
val1 = val2
val2 = temp

print("After Swapping:", "val1 =", val1, "val2 =", val2)


# ------------------------------------------
# 6. Swapping Without Third Variable
# ------------------------------------------

val1 = int(input("Enter the first value: "))
val2 = int(input("Enter the second value: "))

print("Before Swapping:", val1, val2)

val1, val2 = val2, val1

print("After Swapping:", val1, val2)


# ------------------------------------------
# 7. Marks, Percentage & Placement Eligibility
# ------------------------------------------

m = 100
p = 99
c = 88

total = m + p + c
percentage = total * 100 / 300

print("Total Marks:", total)
print("Percentage:", percentage)

if m >= 40 and p >= 40 and c >= 40:
    print("Pass")
else:
    print("Fail")

if percentage >= 60 and total >= 100:
    print("You are eligible for placement")
else:
    print("You are not eligible")


# ------------------------------------------
# 8. Character Checking
# Upper Case / Lower Case / Digit / Special Character
# ------------------------------------------

ch = ord(input("Enter any single character: "))

if ch >= 65 and ch <= 90:
    print("Upper Case")
elif ch >= 97 and ch <= 122:
    print("Lower Case")
elif ch >= 48 and ch <= 57:
    print("Digit")
else:
    print("Special Character")


# ------------------------------------------
# 9. for Loop with range()
# ------------------------------------------

for i in range(10):
    print(i)


for i in range(1, 11):
    print(i)


for i in range(1, 10, 2):
    print(i)


# ------------------------------------------
# 10. Multiplication
# ------------------------------------------

for i in range(1, 11):
    print(i * 1)

for i in range(1, 11):
    print(i * 2)


# ------------------------------------------
# 11. Nested Loop
# ------------------------------------------

for i in range(1, 21):
    print(i, end=" ")

    for j in range(1, 11):
        print(i * j, end=" ")

    print()


# ------------------------------------------
# 12. Array / List Input
# ------------------------------------------

N = int(input("Enter the value of N: "))

array = []

for i in range(N):
    value = int(input())
    array.append(value)

print("Array:", array)

total = sum(array)
print("Total:", total)