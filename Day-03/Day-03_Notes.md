# Day-03 – Technical Training

## 📚 Functions

Function is a block of code used to perform a particular task.

### Types of Functions

1. **Predefined Function**

   * Already available in Python.
   * Examples: `print()`, `len()`, `type()`, `int()`, `float()`

2. **User Defined Function**

   * Function created by the programmer using `def`.

```python
def add(a, b):
    return a + b
```

## 🔹 Types of Arguments

### 1. Positional Argument

Values are passed according to their position.

```python
add(5, 5)
```

### 2. Keyword Argument

Values are passed using parameter names.

```python
personalinfo(firstname="Suraj", lastname="Mishra")
```

### 3. Default Argument

A default value is given to the parameter. If no value is passed, the default value is used.

```python
def cityname(city="Nashik"):
    print(city)
```

### 4. Variable Length Argument

Used when we want to pass multiple values to a function.

`*` is used for variable length arguments.

```python
def statename(*cityname):
    print(cityname)
```

## 🔹 Return Statement

`return` is used to send a value back from a function.

A function can also return multiple values.

```python
def arithmetic(a, b):
    return a + b, a - b, a * b, a / b
```

## 🔍 Linear Search

Linear Search checks elements **one by one** until the required value is found.

* Time Complexity = **O(N)**
* Space Complexity = **O(1)**

If the value is found, its index is returned.
If the value is not found, `-1` is returned.

## 🔹 Positive and Negative Numbers

A function can be used to count positive and negative numbers in a list.

* If number is greater than or equal to `0` → Positive
* Otherwise → Negative

## 🧮 Calculator Using Functions

Different functions can be created for:

* Addition
* Subtraction
* Multiplication
* Division

A `while` loop can be used to repeatedly display the menu.

`break` is used to exit the loop.

## 🕒 Date and Time

Python provides the `datetime` module for working with date and time.

```python
import datetime
```

`datetime.now()` gives the current date and time.

## 🔢 List `count()`

`count()` is used to find how many times an element occurs in a list.

```python
numbers.count(5)
```

## 🔎 List `index()`

`index()` is used to find the index of an element in a list.

```python
numbers.index(5)
```

## 🔄 List Comparison

Lists can be compared using:

* `==` → checks whether two lists are equal
* `!=` → checks whether two lists are different

## 🔢 Type Conversion

Python provides functions to convert values from one data type to another.

### `int()`

Converts a value into an integer.

### `float()`

Converts a value into a floating-point number.

### `complex()`

Converts a value into a complex number.

### `bool()`

Converts a value into `True` or `False`.

## 📅 Working Day or Weekend

A simple `if-else` condition can be used to check whether a day is a working day or weekend.

* Saturday → Weekend
* Sunday → Weekend
* Other days → Working Day

## 🔗 `zip()` Function

`zip()` is used to combine elements from two or more iterables.

It can be used with a `for` loop.

## ⏭️ `continue` Statement

`continue` skips the current iteration and moves to the next iteration of the loop.

## ➕ Operator Precedence

Python follows operator precedence while evaluating expressions.

Example:

```python
(a + b) * c / d
```

Parentheses are evaluated first.

## ✂️ List Slicing

List slicing is used to access a part of a list.

```python
a[start:stop:step]
```

Example:

```python
a[3:0:-1]
```

It can also be used to update selected elements.

## 📦 2D List / Array

A list can contain other lists.

Example:

```python
arr = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]
```

This is called a **2D list/array**.

## 🔧 Function with List Argument

A list can be passed as an argument to a function.

Changes made to the list inside the function can affect the original list because lists are mutable.

## ⚠️ Mutable Default Argument

A list used as a default argument can keep its previous values between function calls.

Example:

```python
def f(i, values=[]):
    values.append(i)
    print(values)
```

Calling the function multiple times keeps adding values to the same list.

## 🔄 Array/List Shifting

List elements can be shifted from one position to another using a loop.

Example:

```python
arr = [1, 2, 3, 4, 5, 6]

for i in range(1, 6):
    arr[i - 1] = arr[i]
```

## 🎯 Key Learning

Day 03 focused on **Python Functions, Types of Arguments, Return Values, Linear Search, List Operations, Type Conversion, Loops, and basic Problem Solving**.
