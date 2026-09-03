# ==========================================
# DAY 02 - PYTHON PRACTICE
# Technical Training Program
# ==========================================


# ------------------------------------------
# 1. List Indexing & Slicing
# ------------------------------------------

mylist = [2, 4, 6, 8, 9, 1, 5]

# Positive indexing
print(mylist[0])
print(mylist[2])

# Slicing
print(mylist[1:])
print(mylist[1:5])

# Negative indexing
print(mylist[-1])

# Slicing with step
print(mylist[0:6:2])

# Reverse list
print(mylist[::-1])


# ------------------------------------------
# 2. Count Even & Odd Numbers
# Time Complexity = O(N)
# ------------------------------------------

mylist = [2, 4, 6, 8, 9, 1, 5]

even = 0
odd = 0

for i in range(len(mylist)):
    if mylist[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)


# ------------------------------------------
# 3. Move Zeros to the End
# ------------------------------------------

array = [5, 6, 0, 2, 0, 1, 7]

for i in array.copy():
    if i == 0:
        array.remove(i)
        array.append(i)

print("After moving zeros:", array)


# ------------------------------------------
# 4. Find Maximum & Minimum
# ------------------------------------------

arr = [5, 3, 9, 2, 8]

maximum = arr[0]
minimum = arr[0]

for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]

    if arr[i] < minimum:
        minimum = arr[i]

print("Minimum:", minimum)
print("Maximum:", maximum)


# ------------------------------------------
# 5. Find Second Largest Element
# ------------------------------------------

array = [7, 3, 9, 2, 8]

array.sort()

print("Sorted Array:", array)
print("Second Largest:", array[-2])


# ------------------------------------------
# 6. Factorial using Recursion
# ------------------------------------------

def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num - 1)


print("Factorial:", factorial(4))


# ------------------------------------------
# 7. Power using Recursion
# ------------------------------------------

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


print("2^0 =", power(2, 0))
print("2^2 =", power(2, 2))
print("2^4 =", power(2, 4))


# ------------------------------------------
# 8. Product of Array using Recursion
# ------------------------------------------

def product_of_array(arr):
    if len(arr) == 0:
        return 1

    return arr[0] * product_of_array(arr[1:])


print("Product:", product_of_array([1, 2, 3]))
print("Product:", product_of_array([1, 2, 3, 10]))


# ------------------------------------------
# 9. Fibonacci using Generator
# ------------------------------------------

def fibonacci_generator(n):
    a, b = 0, 1

    for _ in range(n):
        yield a
        a, b = b, a + b


print("Fibonacci Series:")
print(list(fibonacci_generator(10)))


# ------------------------------------------
# 10. Fibonacci using Iteration
# ------------------------------------------

def fibonacci(n):

    if n <= 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


n = int(input("Enter n: "))
print("Fibonacci:", fibonacci(n))
