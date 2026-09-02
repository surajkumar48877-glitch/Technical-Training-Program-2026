# Day 01 – Technical Training

## 📚 Data Structure

Data Structure are different ways of organizing data on your computer, that can be used effectively.

### Important Points

* Correctness
* Efficiency

---

## 🔄 Data Processing

**INPUT (Data) → PROCESSING → OUTPUT (Information)**

### Example:

**Input:**
`35, 34, 32, 36, Monday, Tuesday, Wednesday, Thursday, Friday`

**Processing:**

* Arranging
* Sorting
* Combining
* Mathematical Operation

**Output:**
Useful Information

---

## 🐍 Python

### Why Python is Dynamically Typed Language?

Python is a dynamically typed language because we don't need to declare a variable's data type explicitly.

The type is determined automatically at **runtime** based on the value assigned to it.

### Example:

```python
math = 50        # int
name = "Suraj"   # str
pi = 3.14        # float
```

---

## 🔢 How to Check the Address of a Variable?

By using `id()` we can check the address/identity of a variable.

```python
print(id(math))
print(id(name))
print(id(pi))
```

---

## 🔄 Reverse a 3-Digit Number

Example:

`123 → 321`

Logic:

```text
123
↓
3 → 2 → 1
↓
321
```

---

## 🔄 Reverse a 6-Digit Number

Example:

`123456 → 654321`

For getting the last digit:

```python
a = num % 10
```

For removing the last digit:

```python
num = num // 10
```

---

## 🔁 Swapping Two Numbers

### Using Third Variable

```python
temp = val1
val1 = val2
val2 = temp
```

Example:

```text
Before:
val1 = 100
val2 = 200

After:
val1 = 200
val2 = 100
```

### Without Using Third Variable

Topic covered in class: **Swapping of two numbers without using third variable.**

---

## 📊 Marks & Placement Eligibility

Program requirements:

* Accept 3 paper marks
* Calculate total
* Calculate percentage
* Check all subjects marks ≥ 40 → **Pass**
* Otherwise → **Fail**
* If percentage ≥ 60 and total ≥ 100 → **Eligible for Placement Drive**
* Otherwise → **Not Eligible**

---

## 🔤 Character Checking

Accept one character and check whether it is:

* Upper Case
* Lower Case
* Digit
* Special Character

### ASCII Values Used

```text
A = 65
Z = 90

a = 97
z = 122

0 = 48
9 = 57
```

Python function used:

```python
ord()
```

---

## 🔁 for Loop

### `range(10)`

```python
for i in range(10):
    print(i)
```

Output:

```text
0 1 2 3 4 5 6 7 8 9
```

### `range(1, 11)`

```python
for i in range(1, 11):
    print(i)
```

Output:

```text
1 2 3 4 5 6 7 8 9 10
```

### `range(start, stop, step)`

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```text
1 3 5 7 9
```

---

## ✖️ Multiplication Table / Nested Loop

Nested loop means **one loop inside another loop**.

Example:

```python
for i in range(1, 21):
    print(i, end=" ")

    for j in range(1, 11):
        print(i * j, end=" ")

    print()
```

---

## 📋 Array / List Input

Accept `N` values from the user and store them in an array/list.

```python
N = int(input("Enter the value of N:"))

array = []

for i in range(N):
    value = int(input())
    array.append(value)

print(array)
```

### Total of Array

```python
total = sum(array)
print(total)
```

### Important Functions Used

* `input()` → User se input lene ke liye
* `int()` → Input ko integer mein convert karne ke liye
* `append()` → List mein value add karne ke liye
* `sum()` → Total calculate karne ke liye
* `range()` → Loop ke liye
* `ord()` → Character ka ASCII value nikalne ke liye
* `id()` → Variable ki identity/address check karne ke liye
* `%` → Remainder nikalne ke liye
* `//` → Integer/Floor division ke liye

---

## 📝 Day 01 Summary

Today I covered:

* Data Structure
* Data Processing
* Python Dynamic Typing
* `type()` function
* `id()` function
* Reverse Number
* Swapping Numbers
* `if-elif-else`
* ASCII Values
* `ord()` function
* `for` loop
* `range()`
* Nested Loop
* List/Array Input
* Sum of Array
* Basic Python Problem Solving
