# ==========================================
# DAY-03 – TECHNICAL TRAINING
# Functions, Linear Search & Python Practice
# ==========================================


# ==========================================
# 1. FUNCTION – POSITIONAL ARGUMENT
# ==========================================

def add(val1, val2):
    print(val1 + val2)


add(5, 5)


# ==========================================
# 2. FUNCTION WITH RETURN
# ==========================================

def add_return(val1, val2):
    return val1 + val2


result = add_return(5, 5)
print("Add =", result)


# ==========================================
# 3. FUNCTION RETURNING MULTIPLE VALUES
# ==========================================

def arithmetic(val1, val2):
    addition = val1 + val2
    subtraction = val1 - val2
    multiplication = val1 * val2
    division = val1 / val2

    return addition, subtraction, multiplication, division


result = arithmetic(5, 5)
print("Arithmetic Result =", result)


# ==========================================
# 4. KEYWORD ARGUMENT
# ==========================================

def personalinfo(firstname, lastname):
    print("First Name:", firstname)
    print("Last Name:", lastname)


personalinfo(firstname="Suraj", lastname="Mishra")


# ==========================================
# 5. DEFAULT ARGUMENT
# ==========================================

def cityname(city="Nashik"):
    print("City Name =", city)


cityname("Mumbai")
cityname("Pune")
cityname()


# ==========================================
# 6. VARIABLE LENGTH ARGUMENT
# ==========================================

def statename(*cityname):
    print("City Name =", cityname)


statename("Mumbai", "Pune", "Nashik", "Nagpur")


# ==========================================
# 7. LINEAR SEARCH
# Time Complexity: O(N)
# Space Complexity: O(1)
# ==========================================

def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target:
            return index

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 7

result = linear_search(array, target)

if result == -1:
    print("Value not found")
else:
    print("Value found at index:", result)


# ==========================================
# 8. COUNT POSITIVE AND NEGATIVE NUMBERS
# ==========================================

def positive_negative(array):
    positive = 0
    negative = 0

    for i in range(len(array)):
        if array[i] >= 0:
            positive += 1
        else:
            negative += 1

    print("Positive =", positive)
    print("Negative =", negative)


array = [3, -2, 7, -1, 0, 5, -4]

positive_negative(array)


# ==========================================
# 9. SIMPLE CALCULATOR USING FUNCTIONS
# ==========================================

def addition(a, b):
    print("Addition =", a + b)


def subtraction(a, b):
    print("Subtraction =", a - b)


def multiplication(a, b):
    print("Multiplication =", a * b)


def division(a, b):
    print("Division =", a / b)


while True:

    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice = "))

    if choice == 1:
        addition(5, 5)

    elif choice == 2:
        subtraction(5, 5)

    elif choice == 3:
        multiplication(5, 5)

    elif choice == 4:
        division(5, 5)

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid Input")


# ==========================================
# 10. DATETIME FORMATTING
# ==========================================

import datetime

date = datetime.datetime.now()

print("It's now: {:%d/%m/%y %H %M %S}".format(date))


# ==========================================
# 11. LIST COUNT()
# ==========================================

numbers = [1, 2, 3, 5, 5, 5, 1, 2, 4, 4, 6, 6, 6]

for value in range(1, 8):
    print(value, "count =", numbers.count(value))


# ==========================================
# 12. LIST index()
# ==========================================

numbers = [1, 2, 3, 5, 5, 5, 1, 2, 4, 4, 6, 6, 6]

for value in range(1, 7):
    print(value, "index =", numbers.index(value))


# ==========================================
# 13. COMPARE TWO LISTS
# ==========================================

x = ['a', 'b', 'c']
y = ['a', 'b', 'c']
z = [1, 2, 3, 4]

print(x == y)
print(x == z)
print(x != z)


# ==========================================
# 14. DATA TYPE CONVERSION – int()
# ==========================================

print(int(3.14))
print(int(True))
print(int(False))
print(int("4"))


# ==========================================
# 15. DATA TYPE CONVERSION – float()
# ==========================================

print(float(3))
print(float(True))
print(float(False))
print(float(4.22))
print(float("4"))


# ==========================================
# 16. DATA TYPE CONVERSION – complex()
# ==========================================

print(complex(3))
print(complex(12.5))
print(complex(True))
print(complex(False))
print(complex(5.6))
print(complex(5, -3))


# ==========================================
# 17. DATA TYPE CONVERSION – bool()
# ==========================================

print(bool(0))
print(bool(15))
print(bool(3.14))
print(bool(0.0))
print(bool(1 + 2j))
print(bool(0 + 0j))
print(bool(-1))
print(bool(True))
print(bool(False))


# ==========================================
# 18. WORKING DAY OR WEEKEND
# ==========================================

day = input("Enter day = ").lower()

if day == "saturday" or day == "sunday":
    print("Weekend Day")
else:
    print("Working Day")


# ==========================================
# 19. zip() WITH for LOOP
# ==========================================

for i, j in zip(range(1, 6), range(5, 0, -1)):

    if i == 3 and j == 3:
        continue

    print(i, j)


# ==========================================
# 20. continue STATEMENT
# ==========================================

for i in range(1, 6):

    if i == 3:
        continue

    print(i, 6 - i)


# ==========================================
# 21. OPERATOR PRECEDENCE
# ==========================================

a = 50
b = 30
c = 20
d = 10

print((a + b) * c / d)
print((a - b) * (c / d))
print(a + (b * c) / d)


# ==========================================
# 22. LIST SLICING AND UPDATING
# ==========================================

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a[::2] = 10, 20, 30, 40, 50

print(a)


# ==========================================
# 23. REVERSE SLICING
# ==========================================

a = [1, 2, 3, 4, 5]

print(a[3:0:-1])


# ==========================================
# 24. FUNCTION WITH LIST ARGUMENT
# ==========================================

def fun(value, values):
    var = 1
    values[0] = 44


t = 3
v = [1, 2, 3]

fun(t, v)

print(t, v[0])


# ==========================================
# 25. 2D LIST / ARRAY
# ==========================================

arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

for i in range(4):
    print(arr[i].pop())


# ==========================================
# 26. MUTABLE DEFAULT ARGUMENT
# ==========================================

def f(i, values=[]):
    values.append(i)
    print(values)


f(1)
f(2)
f(3)


# ==========================================
# 27. LEFT SHIFT OF ARRAY ELEMENTS
# ==========================================

arr = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):
    arr[i - 1] = arr[i]

for i in range(6):
    print(arr[i], end=" ")

print()
