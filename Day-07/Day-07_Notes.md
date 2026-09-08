# Day 07 – Python Notes

## 🔹 Tree

* Tree is a **non-linear data structure**.
* It represents data in a **hierarchical relationship**.
* A tree contains **nodes** connected with each other.
* The first/top node is called the **Root Node**.
* A node can have **children**.
* Tree does not contain a cycle.

### Example

```text
          A
        /   \
       B     C
      / \     \
     D   E     F
```

### Advantages of Tree

* Quicker and easier access to data.
* Used to store hierarchical data.
* Used for:

  * Folder structure
  * Organization structure
  * XML / HTML data

---

# 🔹 Binary Tree

* A Binary Tree is a tree in which each node has **at most two children**.
* These children are called:

  * **Left Child**
  * **Right Child**

### Example

```text
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
```

* Binary Tree is a family of different data structures.
* Examples:

  * Binary Search Tree (BST)
  * Heap Tree
  * AVL Tree
  * Red-Black Tree
  * Syntax Tree

### Where Binary Tree is Used

Binary trees can be used in:

* Huffman Coding
* Heap / Priority problems
* Expression Parsing

Binary Tree is also a basic/prerequisite concept for advanced trees such as BST, AVL and Red-Black Tree.

---

# 🔹 Ways to Implement Binary Tree

There are two common ways:

1. **Linked List**
2. **Python List (Array)**

---

## 🔹 Binary Tree Using Linked List

Each node stores:

```text
[Data | Left | Right]
```

Example:

```text
             Drinks
            /      \
          Hot      Cold
         /   \     /   \
       Tea Coffee Mazza Sprite
```

---

## 🔹 Binary Tree Using Python List

For a binary tree stored using an array/list:

* Left child index = `2 × i`
* Right child index = `2 × i + 1`

For example, if a node is at index `3`:

```text
Left Child  = 2 × 3 = 6
Right Child = 2 × 3 + 1 = 7
```

So:

```text
             3
           /   \
          6     7
```

> This formula assumes **1-based indexing**.

---

# 🔹 Binary Search Tree (BST)

* BST means **Binary Search Tree**.
* In the left subtree, values are **less than or equal to** the parent node.
* In the right subtree, values are **greater than** the parent node.

### Example

```text
             50
           /    \
         30      90
        /  \    /  \
      20   40  60   100
                \
                 80
```

### BST Rule

```text
Left Subtree  → Smaller / Equal Value
Root Node     → Current Value
Right Subtree → Greater Value
```

### Why Binary Search Tree?

* Searching can be faster than a normal Binary Tree when the BST is reasonably balanced.
* Insertion and deletion can also be efficient.

---

# 🔹 Tree Terminology

### Root Node

* The top/first node of a tree.

### Parent Node

* A node that has one or more children.

### Child Node

* A node connected below another node.

### Left Subtree

* The subtree present on the left side of a node.

### Right Subtree

* The subtree present on the right side of a node.

### Level

Example:

```text
             N1          → Level 1
           /    \
         N2      N3      → Level 2
        /  \
      N4    N5            → Level 3
```

---

# 🔹 Tree Traversal

Traversal means **visiting all nodes of a tree**.

There are three important depth-first traversals:

### 1. Inorder

```text
Left → Root → Right
```

### 2. Preorder

```text
Root → Left → Right
```

### 3. Postorder

```text
Left → Right → Root
```

### Example

```text
          A
        /   \
       B     C
      / \
     D   E
```

**Inorder:**

```text
D → B → E → A → C
```

**Preorder:**

```text
A → B → D → E → C
```

**Postorder:**

```text
D → E → B → C → A
```

---

# 🔹 Tree Operations

Important operations on a tree:

* Create a tree
* Insert a node
* Delete a node
* Search for a value
* Traverse all nodes
* Delete the tree

---

# 🔹 Tuple Practice

### Empty Tuple

```python
t = ()
```

Length of an empty tuple is `0`.

### Tuple Without Parentheses

```python
t = "a", "b"
```

This is also a tuple.

### Tuple Concatenation

```python
a = ("1", "2")
b = ("3", "4")

print(a + b)
```

Output:

```text
('1', '2', '3', '4')
```

### Single Element Tuple

```python
t = ("python",)
```

The comma is important.

```python
type(("python",))   # tuple
type(("python"))    # str
```

### Tuple is Immutable

Tuple elements cannot be changed after creation.

```python
t = (1, 2, 3)

# t[0] = 5   # TypeError
```

---

# 🔹 String Practice

### Remove Special Character

If `*` is present in a string, it can be removed using a loop.

Example:

```text
prashant*is*a*good*programmer
```

After removing `*`:

```text
prashantisagoodprogrammer
```

### Character Frequency

Example:

```text
Input:  aabbbbeeeeffggg
Output: a2b4e4f2g3
```

This means:

* `a` → 2 times
* `b` → 4 times
* `e` → 4 times
* `f` → 2 times
* `g` → 3 times
