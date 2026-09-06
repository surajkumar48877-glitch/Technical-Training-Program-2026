# Day 05 – Python Notes

## 🔹 String Problems

### Palindrome

* A string is a palindrome if it is the same from both sides.
* Example: `madam` → Palindrome
* Use `[::-1]` to reverse a string.

### Vowels and Consonants

* Vowels: `a, e, i, o, u`
* Other alphabets are consonants.
* Convert the string to lowercase using `lower()`.

### Anagram

* Two strings are anagrams if they contain the same characters.
* Example: `silent` and `listen` → Anagram.

### Count Words

* Count the spaces and add `1`.
* Example: `"This is a sentence"` → `4` words.

### Reverse Words

* Split the string into words.
* Reverse the words using slicing.
* Example: `"Hello world"` → `"world Hello"`.

### Special Characters

* `isalnum()` checks alphabet and number.
* If `isalnum()` is `False`, it is a special character.

---

## 🔹 Dictionary

* Dictionary stores data in **key : value** form.
* Keys should be unique.
* Duplicate keys are replaced by the latest value.

### Dictionary Methods

* `keys()` → returns keys
* `values()` → returns values
* `items()` → returns key-value pairs
* `pop()` → removes a key-value pair
* `clear()` → removes all elements
* `copy()` → creates a copy
* `get()` → gets value using key

### Dictionary Loop

```python
for i in student:
    print(i)
```

Prints keys.

```python
for i in student.values():
    print(i)
```

Prints values.

```python
for i in student.items():
    print(i)
```

Prints key-value pairs.

### Dictionary Key Examples

* `1` and `"1"` are different keys.
* `1` and `1.0` are treated as the same key.
* Tuple can be used as a dictionary key.

---

## 🔹 Queue

* Queue follows **FIFO**.
* FIFO = **First In First Out**.

### Queue Operations

* **Enqueue** → add element
* **Dequeue** → remove first element
* **Peek Front** → show first element
* **isEmpty** → check queue is empty
* **isFull** → check queue is full
* **Display** → show queue elements
* **Delete Queue** → delete/clear queue

### Queue using List

* Queue can be implemented using Python List.
* `append()` is used to add an element.
* `pop(0)` is used to remove the first element.

## 📝 Key Learning

Day 05 focused on String Problems, Dictionary Operations, and Queue implementation using Python.
