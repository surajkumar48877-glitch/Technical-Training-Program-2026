# ============================================================
# DAY 07 - TREE, BST, TUPLE & STRING PRACTICE
# ============================================================


# ============================================================
# 1. GENERAL TREE
# ============================================================

class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, child):
        self.children.append(child)

    def show(self, level=0):
        print(" " * level + str(self.data))

        for child in self.children:
            child.show(level + 1)

    def search(self, value):
        if self.data == value:
            return True

        for child in self.children:
            if child.search(value):
                return True

        return False


# -------------------- Tree Creation --------------------

root = Tree("Sandip University")

bca = Tree("BCA")
bsc = Tree("BSC")

root.add(bca)
root.add(bsc)

bca.add(Tree("Python"))
bca.add(Tree("Java"))

bsc.add(Tree("R-Programming"))
bsc.add(Tree("ML"))


# -------------------- Traverse --------------------

print("Tree:")
root.show()


# -------------------- Search --------------------

print("\nSearch Python:", root.search("Python"))


# -------------------- Insert Node --------------------

bca.add(Tree("DBMS"))

print("\nAfter Insertion:")
root.show()


# -------------------- Delete Node --------------------

# Delete Java
bca.children.pop(1)

print("\nAfter Deletion:")
root.show()


# -------------------- Delete Complete Tree --------------------

root = None

print("\nTree Deleted:", root)


# ============================================================
# 2. TUPLE PRACTICE
# ============================================================

print("\n" + "=" * 50)
print("TUPLE PRACTICE")
print("=" * 50)


# Empty Tuple
init_tuple = ()

print("Length of empty tuple:", len(init_tuple))


# Tuple without parentheses
init_tuple_a = "a", "b"
init_tuple_b = ("a", "b")

print("Tuples are equal:", init_tuple_a == init_tuple_b)


# Tuple concatenation
init_tuple_a = ("1", "2")
init_tuple_b = ("3", "4")

print("Tuple concatenation:", init_tuple_a + init_tuple_b)


# Repeating tuple
init_tuple = ("python",) * 3

print("Repeated tuple:", init_tuple)


# Check tuple type
init_tuple = ("python",) * 3

print("Type:", type(init_tuple))


# String type
init_tuple = ("python") * 3

print("Type without comma:", type(init_tuple))


# Tuple immutability
init_tuple = (1,) * 3

print("Original tuple:", init_tuple)

# init_tuple[0] = 2
# TypeError because tuple is immutable


# Tuple slicing
init_tuple = ((1, 2),) * 7

print("Length after slicing:", len(init_tuple[3:8]))


# ============================================================
# 3. REMOVE '*' FROM STRING
# ============================================================

print("\n" + "=" * 50)
print("REMOVE SPECIAL CHARACTER")
print("=" * 50)

name = "prashant*is*a*good*programmer"

newname = ""

for char in name:
    if char != "*":
        newname += char

print("Original:", name)
print("After removing *:", newname)


# ============================================================
# 4. CHARACTER FREQUENCY
# ============================================================

print("\n" + "=" * 50)
print("CHARACTER FREQUENCY")
print("=" * 50)

s = "aabbbbeeeeffggg"

answer = ""

i = 0

while i < len(s):
    count = 1

    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1

    answer += s[i] + str(count)
    i += 1

print("Input :", s)
print("Output:", answer)


# ============================================================
# 5. CHARACTER FREQUENCY USING DICTIONARY
# ============================================================

name = "aabbbbeeeeffggg"

frequency = {}

for char in name:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("\nFrequency Dictionary:")

for char, count in frequency.items():
    print(char, count, sep=" ", end=" ")


# ============================================================
# 6. BINARY SEARCH TREE (BST)
# ============================================================

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


def insert_node(root_node, node_value):
    # Empty root
    if root_node.data is None:
        root_node.data = node_value

    # Insert on left side
    elif node_value <= root_node.data:

        if root_node.leftchild is None:
            root_node.leftchild = BSTNode(node_value)

        else:
            insert_node(root_node.leftchild, node_value)

    # Insert on right side
    else:

        if root_node.rightchild is None:
            root_node.rightchild = BSTNode(node_value)

        else:
            insert_node(root_node.rightchild, node_value)


# ============================================================
# 7. PREORDER TRAVERSAL
# ============================================================

def preorder_traversal(root_node):

    if root_node is None:
        return

    # Root
    print(root_node.data, end=" ")

    # Left
    preorder_traversal(root_node.leftchild)

    # Right
    preorder_traversal(root_node.rightchild)


# ============================================================
# 8. CREATE BST
# ============================================================

new_bst = BSTNode(None)

insert_node(new_bst, 70)
insert_node(new_bst, 50)
insert_node(new_bst, 90)
insert_node(new_bst, 30)
insert_node(new_bst, 60)
insert_node(new_bst, 80)
insert_node(new_bst, 100)
insert_node(new_bst, 20)
insert_node(new_bst, 40)


# ============================================================
# 9. DISPLAY BST USING PREORDER
# ============================================================

print("\n\nBST Preorder Traversal:")

preorder_traversal(new_bst)

print()
