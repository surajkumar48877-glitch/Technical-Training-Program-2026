# ============================================================
# DAY 10 - PYTHON PROBLEM SOLVING
# ============================================================


# ============================================================
# 1. FIND DUPLICATE VALUES AND THEIR COUNT
# ============================================================

my_list = [5, 7, 2, 3, 7, 8, 2, 3, 3]

new_dict = {}

for i in range(len(my_list)):
    count = 0
    key = my_list[i]

    for j in range(len(my_list)):
        if key == my_list[j]:
            count += 1

    if count > 1:
        new_dict[key] = count

print("Duplicate values and their count:")
print(new_dict)


# ============================================================
# 2. SEPARATE EVEN AND ODD NUMBERS
# ============================================================

n = int(input("\nEnter the number of values: "))

my_list = []

for i in range(n):
    value = int(input("Enter the value: "))
    my_list.append(value)

even_numbers = []
odd_numbers = []

for value in my_list:
    if value % 2 == 0:
        even_numbers.append(value)
    else:
        odd_numbers.append(value)

print("Even:", even_numbers)
print("Odd:", odd_numbers)

print("All even numbers followed by odd numbers:")
print(*(even_numbers + odd_numbers))


# ============================================================
# 3. FIND MAXIMUM PRODUCT OF TWO VALUES
# ============================================================

my_list = [7, 9, -3, 8, -6, -7, 8, 10]

largest_product = my_list[0] * my_list[1]

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        product = my_list[i] * my_list[j]

        if product > largest_product:
            largest_product = product

print("\nMaximum product:", largest_product)


# ============================================================
# 4. EMPLOYEE DISTANCE RANGE PROBLEM
# ============================================================

x, y, z = map(int, input(
    "\nEnter number of employees, minimum distance and maximum distance: "
).split())

my_list = []

for i in range(x):
    distance = int(input("Enter distance: "))
    my_list.append(distance)

print("Employees within the given range:")

for distance in my_list:
    if y <= distance <= z:
        print(distance, end=" ")

print()


# ============================================================
# 5. FIND PERFECT SQUARE VALUES
# ============================================================

n = int(input("\nEnter the number of values: "))

my_list = []

for i in range(n):
    value = int(input("Enter the value: "))
    my_list.append(value)

print("Perfect square values:")

for i in range(1, n + 1):
    square = i * i

    if square in my_list:
        print(square)
