# Day 02 – Technical Training

## 📌 Time Complexity

**Time Complexity** tells us how much time an algorithm takes as the input size increases.

### Three Important Cases

* **Best Case** → Minimum time taken
* **Average Case** → Average time taken
* **Worst Case** → Maximum time taken

---

## 🔹 Big-O — O()

Big-O is used to describe the **upper bound / worst-case complexity** of an algorithm.

Example:

```text
O(1)   → Constant
O(N)   → Linear
O(N²)  → Quadratic
O(log N) → Logarithmic
```

---

## 🔹 Big-Omega — Ω()

Big-Omega describes the **lower bound / best-case complexity**.

---

## 🔹 Big-Theta — Θ()

Big-Theta describes the **tight bound**, when the upper and lower bounds are of the same order.

---

## ⏱️ Common Time Complexities

### O(1) – Constant Time

Accessing a specific element in an array/list.

```python
array = [1, 2, 3, 4, 5]

print(array[0])
```

It takes constant time because we directly access the element.

---

### O(N) – Linear Time

Visiting every element in an array/list.

```python
array = [1, 2, 3, 4, 5]

for element in array:
    print(element)
```

It is linear time because every element is visited.

---

### O(log N) – Logarithmic Time

The input is reduced in steps.
Example: Binary Search.

---

### O(N²) – Quadratic Time

Nested loop where each element is compared with every other element.

```python
array = [1, 2, 3, 4, 5]

for x in array:
    for y in array:
        print(x, y)
```

---

## 🔨 Brute Force Algorithm

Brute Force simply tries **all possible possibilities** until a satisfactory solution is found.

---

## 🎲 Randomized Algorithm

Randomized Algorithm uses **random values/numbers** at least once during computation to make a decision.

---

# 🔁 Recursion

Recursion is a way of solving a problem where a **function calls itself**.

### Important Points

* Same operation is performed multiple times with different inputs.
* In every step, we try to make the problem smaller.
* **Base condition is required** to stop recursion.
* Without a base condition, infinite recursion can occur.

---

## 🧮 Factorial using Recursion

Example:

```text
4! = 4 × 3 × 2 × 1
   = 24
```

---

## ⚡ Power using Recursion

Example:

```text
2⁴ = 2 × 2 × 2 × 2
   = 16
```

---

## 🔄 Recursion vs Iteration

| Point              | Recursion            | Iteration           |
| ------------------ | -------------------- | ------------------- |
| Space Efficient    | No                   | Yes                 |
| Extra Stack Memory | Required             | Not required        |
| Time Efficient     | Usually less         | Usually better      |
| Easy to Code       | Yes                  | Depends             |
| Best Use           | Similar sub-problems | Repeated operations |

### Important Point

Recursion uses **stack memory** because every function call is stored in the call stack.

---

# 📋 List / Array Operations

Day 2 mein list/array ke following operations practice kiye:

* Accessing elements
* Positive indexing
* Negative indexing
* Slicing
* Reverse slicing
* Counting even and odd numbers
* Moving zeros to the end
* Finding maximum and minimum
* Finding second largest element
* Removing duplicates
* Finding missing number
* Product of array elements

---

## 🔢 List Indexing

Example:

```python
mylist = [2, 4, 6, 8, 9, 1, 5]
```

Positive Index:

```text
 0  1  2  3  4  5  6
 2  4  6  8  9  1  5
```

Negative Index:

```text
-7 -6 -5 -4 -3 -2 -1
 2  4  6  8  9  1  5
```

---

## ✂️ List Slicing

```python
mylist[1:]
mylist[1:5]
mylist[0:6:2]
mylist[::-1]
```

`[::-1]` is used to reverse a list.

---

# 🔢 Even & Odd Count

Count the number of even and odd elements in a list.

Time Complexity:

```text
O(N)
```

because we visit every element.

---

# 🔄 Move Zeros to End

Example:

```text
Input  → [5, 6, 0, 2, 0, 1, 7]

Output → [5, 6, 2, 1, 7, 0, 0]
```

---

# 🔝 Maximum & Minimum

Find the maximum and minimum elements from an array/list.

Example:

```text
[5, 3, 9, 2, 8]

Maximum = 9
Minimum = 2
```

---

# 🥈 Second Largest Element

```python
array.sort()
print(array[-2])
```

After sorting, `-2` gives the second last element.

---

# ✖️ Product of Array using Recursion

Example:

```text
[1, 2, 3]

1 × 2 × 3 = 6
```

---

# 🐇 Fibonacci Series

Fibonacci series:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Each next number is obtained by adding the previous two numbers.

### Using Iteration

```python
a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b
```

### Using Recursion

Fibonacci can also be implemented using recursion.

---

# 📝 Day 02 Summary

Today I covered:

* Time Complexity
* Best, Average & Worst Case
* Big-O, Big-Ω & Big-Θ
* O(1), O(N), O(log N), O(N²)
* Brute Force Algorithm
* Randomized Algorithm
* Recursion
* Base Condition
* Recursion vs Iteration
* List Indexing & Slicing
* Even/Odd Count
* Moving Zeros
* Maximum & Minimum
* Second Largest
* Product of Array
* Fibonacci
