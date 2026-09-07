# Day 06 – Python Notes

## 🔹 Instance Variable

* Instance variables depend on the **object**.
* Each object can have its own value.
* Instance variable is created using `self`.

Example:

```python
class Employee:
    def __init__(self):
        self.name = "Suraj"
```

Here, `name` is an instance variable.

### Important

* Different objects can have different values.
* We can add or delete an instance variable using an object.
* `__dict__` shows the instance variables of an object.

---

## 🔹 Static Variable

* Static variables do **not depend on a particular object**.
* They belong to the class.
* Static variable is generally created inside the class but outside methods.
* One common value can be shared by objects.

Example:

```python
class College:
    college_name = "Sandip University"
```

Here, `college_name` is a static variable.

### Important

* Static variable can be accessed using the class or object.
* Value can be changed using the class name.

```python
College.college_name = "Modern University"
```

---

## 🔹 Instance Variable vs Static Variable

| Instance Variable                  | Static Variable                        |
| ---------------------------------- | -------------------------------------- |
| Depends on object                  | Does not depend on a particular object |
| Created using `self`               | Created inside class                   |
| Each object can have its own value | Common value can be shared             |
| Example: `self.name`               | Example: `college_name`                |

---

# 🔹 Linked List

* Linked List is a form of **sequential collection**.
* It does not have to be stored in order.
* A Linked List is made up of **independent nodes**.
* A node can contain any type of data.
* Each node has a **reference to the next node**.

### Node

A node mainly contains:

```text
[Data | Next]
```

Example:

```text
[10 | Next] -> [20 | Next] -> [30 | None]
```

* `data` → stores the value.
* `next` → stores the reference of the next node.
* `head` → points to the first node.
* `None` → shows that there is no next node.

---

## 🔹 Creating a Node

```python
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
```

---

## 🔹 Linked List

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

* `head = None` means the linked list is empty.

---

## 🔹 Adding Node at Beginning

* Create a new node.
* Connect the new node with the current head.
* Make the new node the new head.

Example:

```text
Before:
[10] -> [20] -> None

After adding 5:
[5] -> [10] -> [20] -> None
```

---

## 🔹 Adding Node at End

* Create a new node.
* Connect the last node with the new node.
* Make the new node the new tail.

Example:

```text
[10] -> [20] -> [30] -> None
```

---

## 🔹 Display Linked List

* Start from `head`.
* Print the data.
* Move to the next node using `next`.
* Continue until `None`.

```python
while head != None:
    print(head.data)
    head = head.next
```

## 📝 Key Learning

Day 06 focused on Instance Variables, Static Variables, and Linked List implementation using Nodes.
