# Day 09 – Python Notes

## 🔹 List Comprehension

List comprehension is used to create a list in a simple and short way.

### Example:

```python
s = [i * i for i in range(1, 11)]
print(s)
```

**Output:**

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

### Power using List Comprehension

```python
val = [2 ** i for i in range(1, 6)]
print(val)
```

**Output:**

```text
[2, 4, 8, 16, 32]
```

### List Comprehension with Condition

```python
val2 = [i for i in s if i % 2 == 0]
print(val2)
```

**Output:**

```text
[4, 16, 36, 64, 100]
```

---

## 🔹 Dictionary Comprehension

Dictionary comprehension is used to create a dictionary in a simple way.

### Squares

```python
squares = {x: x * x for x in range(1, 6)}
print(squares)
```

**Output:**

```text
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Doubles

```python
doubles = {x: 2 * x for x in range(1, 6)}
print(doubles)
```

**Output:**

```text
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}
```

---

## 🔹 Reading Multiple Values

We can take multiple values from a single input line using `split()`.

### Two Integer Values

```python
a, b = [int(x) for x in input("Enter 2 numbers: ").split()]
print("Product is:", a * b)
```

Example:

```text
Enter 2 numbers: 5 10
Product is: 50
```

### Three Float Values

```python
a, b, c = [float(x) for x in input("Enter 3 float numbers: ").split(",")]
print("The sum is:", a + b + c)
```

Example:

```text
Enter 3 float numbers: 10.5,20.5,30
The sum is: 61.0
```

---

## 🔹 Removing Spaces from String

### 1. `rstrip()`

Removes spaces from the **right side**.

### 2. `lstrip()`

Removes spaces from the **left side**.

### 3. `strip()`

Removes spaces from **both sides**.

Example:

```python
city = "  Mumbai  "

print(city.rstrip())
print(city.lstrip())
print(city.strip())
```

---

## 🔹 String Replace

`replace()` is used to replace one string with another string.

### Syntax:

```python
string.replace(old_string, new_string)
```

Example:

```python
s = "Python is difficult"
s1 = s.replace("difficult", "easy")
print(s1)
```

**Output:**

```text
Python is easy
```

### Replace All Occurrences

```python
s = "abbbabab"
s1 = s.replace("a", "b")
print(s1)
```

**Output:**

```text
bbbbbbbb
```

---

## 🔹 Find Unique Vowels in a Word

We can use a list of vowels and check each character of the word.

```python
vowels = ['a', 'e', 'i', 'o', 'u']
```

If a vowel is already found, we don't add it again.

Example:

```text
Enter the word where we will search the vowels: rahi

found vowels = ['a', 'i']
unique vowels 2 from the given word = rahi
```

---

## 🔹 Adjacency Matrix

* Adjacency Matrix is used to represent a graph.
* It is a 2D matrix.
* `1` means there is an edge.
* `0` means there is no edge.

### When to use?

* If a graph is **complete or almost complete**, use **Adjacency Matrix**.
* If the number of edges is **few**, use **Adjacency List**.

Example:

```text
    A B C
A   0 1 1
B   1 0 0
C   1 0 0
```

---

## 🔹 Static Adjacency Matrix

In this method, the number of vertices is already given.

Example:

```python
graph = Graph(5)
```

The matrix is created using:

```python
self.matrix = [[0] * vertices for _ in range(vertices)]
```

---

## 🔹 Dynamic Adjacency Matrix

In dynamic programming, the number of vertices and edges are taken from the user.

```python
n = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))
```

Then each edge is entered by the user.

---

## 🔹 Key Learning

Day 09 focused on **List Comprehension, Dictionary Comprehension, Multiple Inputs, String Methods, Unique Vowels, and Adjacency Matrix implementation using Python**.
