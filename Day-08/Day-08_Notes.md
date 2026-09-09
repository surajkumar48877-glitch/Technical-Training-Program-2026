# Day 08 – Python Notes

## 🔹 Time Complexity & Space Complexity of BST

| BST Operation      | Time Complexity              | Space Complexity |
| ------------------ | ---------------------------- | ---------------- |
| Create BST         | O(1)                         | O(1)             |
| Insert a Node      | O(log N) average, O(N) worst | O(log N) average |
| Traverse BST       | O(N)                         | O(N)             |
| Search for a Node  | O(log N) average, O(N) worst | O(log N) average |
| Delete a Node      | O(log N) average, O(N) worst | O(log N) average |
| Delete Entire BST* | O(1)                         | O(1)             |

> *If the BST is deleted simply by removing the root/reference. Actually freeing every node one-by-one would take O(N).

---

# 🔹 Graph

* A Graph consists of a finite set of **Vertices (Nodes)** and **Edges**.
* An edge connects a pair of nodes.
* **Vertex/Node** → represents a point.
* **Edge** → represents a connection between nodes.

### Example

```text
        A
       / \
      B---C
       \
        D
```

Here:

* A, B, C, D → Vertices/Nodes
* Lines → Edges

---

# 🔹 Types of Graph

Graphs can be classified based on:

### 1. Directed Graph

* Edges have a direction.

```text
A → B
```

### 2. Undirected Graph

* Edges do not have a direction.

```text
A ─── B
```

### 3. Weighted Graph

* Edges have a weight/value.

```text
A ──5── B
```

### 4. Unweighted Graph

* Edges do not have a weight.

```text
A ─── B
```

### Weight can also be:

* Positive
* Negative

So examples include:

1. Unweighted Undirected
2. Unweighted Directed
3. Positive Weighted Undirected
4. Positive Weighted Directed
5. Negative Weighted Undirected
6. Negative Weighted Directed

---

# 🔹 Adjacency Matrix

* Adjacency Matrix is a **square matrix**.
* It can be represented using a **2D array/list**.
* It shows whether two vertices are connected or not.

Example:

```text
      A  B  C  D
A     0  1  1  0
B     1  0  0  1
C     1  0  0  1
D     0  1  1  0
```

* `1` → edge/connection exists.
* `0` → edge/connection does not exist.

For an undirected graph, the matrix is usually symmetric.

---

# 🔹 Adjacency List

* Adjacency List is a collection of lists used to represent a graph.
* Each list contains the **neighbours** of a vertex.

Example:

```text
A → B → C
B → A → D
C → A → D
D → B → C
```

---

# 🔹 Adjacency List Using Python Dictionary

A Python dictionary can be used to store an adjacency list.

```python
graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "D"],
    "D": ["A", "C", "E"],
    "E": ["B", "D"]
}
```

Here:

* Key → Vertex
* List → Neighbouring vertices

---

# 🔹 BST Operations

Important BST operations:

* Create BST
* Insert a Node
* Search for a Node
* Traverse BST
* Delete a Node
* Delete Entire BST

### BST Rule

```text
          70
        /    \
      50      90
     /  \    /  \
   30   60  80  100
  /  \
20   40
```

* Left subtree → value is less than or equal to parent.
* Right subtree → value is greater than parent.

---

# 🔹 BST Traversal

### Preorder

```text
Root → Left → Right
```

### Inorder

```text
Left → Root → Right
```

### Postorder

```text
Left → Right → Root
```

For the above BST:

```text
Preorder  → 70 50 30 20 40 60 90 80 100
Inorder   → 20 30 40 50 60 70 80 90 100
Postorder → 20 40 30 60 50 80 100 90 70
```

---

# 🔹 Performance Rating Problem

Accept:

* Salary
* Performance rating

Increment salary according to rating:

| Rating   | Salary Increment |
| -------- | ---------------: |
| 1 to 3   |              10% |
| 3.1 to 4 |              20% |
| 4.1 to 5 |              30% |

If rating is outside `1–5`, it is invalid.

---

# 🔹 Maximum Value from Each Row

Given a 2D list, find the maximum value from each row.

Example:

```text
[100, 198, 333, 323] → 333
[122, 232, 221, 111] → 232
[223, 565, 245, 764] → 764
```

Output:

```text
[333, 232, 764]
```

---

# 🔹 Employee Distance Problem

Given:

```text
6 30 50
29 38 12 48 39 55
```

* `6` → number of employees
* `30` → minimum distance
* `50` → maximum distance

Distances between `30` and `50` are:

```text
38 48 39
```

Output:

```text
38 48 39
```

---

## 📝 Key Learning

Day 08 focused on BST Operations, Time and Space Complexity, Graphs, Graph Types, Adjacency Matrix, Adjacency List, and Python problem-solving.
