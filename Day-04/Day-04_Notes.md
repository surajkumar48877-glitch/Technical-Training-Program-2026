# Day-04 – Technical Training

## 📚 Stack

Stack is a data structure that follows **LIFO**.

**LIFO = Last In First Out**

The element inserted last will be removed first.

### 🔹 Stack Operations

* **Push** – Add an element to the stack.
* **Pop** – Remove the top element from the stack.
* **Peek** – Return/display the top element.
* **isEmpty** – Check whether the stack is empty.
* **isFull** – Check whether the stack is full.
* **Display** – Display stack elements.
* **Delete Stack** – Delete the stack.

### 🔹 Stack Using List

Stack can be implemented using a Python list.

* Easy to implement.
* `append()` can be used for push.
* `pop()` can be used for pop.
* Performance can be affected when the list grows.

### 🔹 Stack Using Linked List

Stack can also be implemented using a linked list.

* Good performance.
* Dynamic size.
* Implementation is more difficult compared to a list.

## 🔹 Constructor

A constructor is a special method in a class.

In Python, `__init__()` is used as a constructor.

It is called automatically when an object of the class is created.

## 🔹 Nested Loop

A loop inside another loop is called a nested loop.

* Outer loop → Rows
* Inner loop → Columns

Nested loops are used to create different patterns.

## ⭐ Pattern Printing

Practiced different patterns using:

* Numbers
* Alphabets
* `*` (star)
* Increasing patterns
* Decreasing patterns
* Pyramid patterns
* Reverse patterns

`chr()` can be used with ASCII values to print alphabets.

Example:

```python
chr(65)
```

Output:

```text
A
```

## 🔹 String Formatting

Python provides different ways to format strings.

* `.format()`
* `f-string`
* `zfill()`

Example:

```python
"7".zfill(4)
```

Output:

```text
0007
```

## 🔤 String Functions

Important string functions practiced:

* `lower()` – Converts string to lowercase.
* `upper()` – Converts string to uppercase.
* `swapcase()` – Changes uppercase to lowercase and lowercase to uppercase.
* `title()` – Converts first letter of each word to uppercase.
* `capitalize()` – Converts first character to uppercase.
* `join()` – Joins multiple strings.
* `find()` – Finds the position of a substring.
* `isalnum()` – Checks letters and numbers.
* `isalpha()` – Checks alphabets.
* `isdigit()` – Checks digits.
* `islower()` – Checks lowercase.
* `isupper()` – Checks uppercase.
* `istitle()` – Checks title case.
* `isspace()` – Checks whitespace.
* `startswith()` – Checks starting characters.
* `endswith()` – Checks ending characters.

## ✂️ String Slicing

String slicing is used to access a part of a string.

```python
string[start:stop:step]
```

Examples:

```python
name[0:4]
name[2:]
name[:4]
name[::-1]
```

## 🔄 String Traversing

A string can be accessed character by character using a `for` loop.

```python
for i in "suraj":
    print(i)
```

String characters can also be accessed using their index.

## 🔁 Reverse String

A string can be printed in reverse using:

```python
name[::-1]
```

or by using a reverse `for` loop.

## 🚫 Remove Duplicate Characters

Duplicate characters can be removed by checking whether the character is already present in a new string.

```python
if i not in newname:
    newname += i
```

## 🎯 Key Learning

Day 04 focused on Stack, Constructor, Nested Loops, Pattern Printing, String Functions, String Slicing, String Traversing and basic Python problem-solving.
