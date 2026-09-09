# ============================================================
# DAY 08 - BST, GRAPH & PYTHON PROBLEM SOLVING
# ============================================================


# ============================================================
# 1. BINARY SEARCH TREE
# ============================================================

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


# ============================================================
# 2. INSERT NODE IN BST
# ============================================================

def insert_node(root_node, node_value):

    if root_node.data is None:
        root_node.data = node_value

    elif node_value <= root_node.data:

        if root_node.leftchild is None:
            root_node.leftchild = BSTNode(node_value)
        else:
            insert_node(root_node.leftchild, node_value)

    else:

        if root_node.rightchild is None:
            root_node.rightchild = BSTNode(node_value)
        else:
            insert_node(root_node.rightchild, node_value)


# ============================================================
# 3. PREORDER TRAVERSAL
# ============================================================

def preorder_traversal(root_node):

    if root_node is None or root_node.data is None:
        return

    print(root_node.data, end=" ")

    preorder_traversal(root_node.leftchild)
    preorder_traversal(root_node.rightchild)


# ============================================================
# 4. INORDER TRAVERSAL
# ============================================================

def inorder_traversal(root_node):

    if root_node is None or root_node.data is None:
        return

    inorder_traversal(root_node.leftchild)

    print(root_node.data, end=" ")

    inorder_traversal(root_node.rightchild)


# ============================================================
# 5. POSTORDER TRAVERSAL
# ============================================================

def postorder_traversal(root_node):

    if root_node is None or root_node.data is None:
        return

    postorder_traversal(root_node.leftchild)
    postorder_traversal(root_node.rightchild)

    print(root_node.data, end=" ")


# ============================================================
# 6. SEARCH NODE IN BST
# ============================================================

def search_node(root_node, node_value):

    if root_node is None or root_node.data is None:
        return False

    if root_node.data == node_value:
        return True

    elif node_value < root_node.data:
        return search_node(root_node.leftchild, node_value)

    else:
        return search_node(root_node.rightchild, node_value)


# ============================================================
# 7. FIND MINIMUM NODE
# ============================================================

def find_minimum(root_node):

    current = root_node

    while current.leftchild is not None:
        current = current.leftchild

    return current


# ============================================================
# 8. DELETE NODE FROM BST
# ============================================================

def delete_node(root_node, node_value):

    if root_node is None:
        return None

    # Search in left subtree
    if node_value < root_node.data:
        root_node.leftchild = delete_node(
            root_node.leftchild,
            node_value
        )

    # Search in right subtree
    elif node_value > root_node.data:
        root_node.rightchild = delete_node(
            root_node.rightchild,
            node_value
        )

    # Node found
    else:

        # Case 1: No child
        if root_node.leftchild is None and root_node.rightchild is None:
            return None

        # Case 2: Only right child
        if root_node.leftchild is None:
            return root_node.rightchild

        # Case 3: Only left child
        if root_node.rightchild is None:
            return root_node.leftchild

        # Case 4: Two children
        successor = find_minimum(root_node.rightchild)

        root_node.data = successor.data

        root_node.rightchild = delete_node(
            root_node.rightchild,
            successor.data
        )

    return root_node


# ============================================================
# 9. DELETE ENTIRE BST
# ============================================================

def delete_bst(root_node):

    return None


# ============================================================
# 10. CREATE BST
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
# 11. BST TRAVERSALS
# ============================================================

print("Preorder:")
preorder_traversal(new_bst)

print("\n\nInorder:")
inorder_traversal(new_bst)

print("\n\nPostorder:")
postorder_traversal(new_bst)


# ============================================================
# 12. SEARCH
# ============================================================

print("\n\nSearch 40:")

if search_node(new_bst, 40):
    print("The value is found")
else:
    print("The value is not found")


# ============================================================
# 13. DELETE NODE
# ============================================================

new_bst = delete_node(new_bst, 40)

print("\nBST after deleting 40:")
preorder_traversal(new_bst)


# ============================================================
# 14. DELETE ENTIRE BST
# ============================================================

new_bst = delete_bst(new_bst)

print("\n\nBST after deleting entire tree:", new_bst)


# ============================================================
# 15. PERFORMANCE RATING - SALARY INCREMENT
# ============================================================

print("\n" + "=" * 50)
print("SALARY INCREMENT")
print("=" * 50)

salary = int(input("Enter your salary: "))
rating = float(input("Enter your performance appraisal rating: "))

increment = 0

if 1 <= rating <= 3:
    increment = salary * 10 / 100

elif 3.1 <= rating <= 4:
    increment = salary * 20 / 100

elif 4.1 <= rating <= 5:
    increment = salary * 30 / 100

else:
    print("Invalid Rating")

if increment > 0:
    increased_salary = salary + increment

    print("Increment:", increment)
    print("Increased Salary:", increased_salary)


# ============================================================
# 16. FIND MAXIMUM VALUE FROM EACH ROW
# ============================================================

my_list = [
    [100, 198, 333, 323],
    [122, 232, 221, 111],
    [223, 565, 245, 764]
]

new_list = []

for row in my_list:

    maximum = row[0]

    for value in row:

        if value > maximum:
            maximum = value

    new_list.append(maximum)

print("\nMaximum value from each row:")
print(new_list)


# ============================================================
# 17. EMPLOYEE DISTANCE PROBLEM
# ============================================================

data = list(map(int, input(
    "\nEnter number of employees, minimum distance and maximum distance: "
).split()))

n = data[0]
minimum_distance = data[1]
maximum_distance = data[2]

distances = list(map(int, input(
    "Enter employee distances: "
).split()))

result = []

for distance in distances:

    if minimum_distance <= distance <= maximum_distance:
        result.append(distance)

print("Employees within the given range:")

for distance in result:
    print(distance, end=" ")


# ============================================================
# 18. GRAPH USING ADJACENCY LIST
# ============================================================

class Graph:

    def __init__(self):
        self.adjacency_list = {}

    # Add vertex
    def add_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            return True

        return False

    # Display graph
    def display_graph(self):

        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    # Add directed edge
    def add_edge(self, vertex1, vertex2):

        if (
            vertex1 in self.adjacency_list
            and vertex2 in self.adjacency_list
        ):
            self.adjacency_list[vertex1].append(vertex2)
            return True

        return False

    # Remove vertex
    def remove_vertex(self, vertex):

        if vertex not in self.adjacency_list:
            return False

        # Remove vertex from neighbours
        for other_vertex in self.adjacency_list:

            if vertex in self.adjacency_list[other_vertex]:
                self.adjacency_list[other_vertex].remove(vertex)

        # Delete vertex
        del self.adjacency_list[vertex]

        return True

    # Remove edge
    def remove_edge(self, vertex1, vertex2):

        if (
            vertex1 in self.adjacency_list
            and vertex2 in self.adjacency_list
        ):

            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)

            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

            return True

        return False


# ============================================================
# 19. CREATE GRAPH
# ============================================================

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")


# ============================================================
# 20. ADD EDGES
# ============================================================

graph.add_edge("A", "B")
graph.add_edge("A", "C")

graph.add_edge("B", "A")
graph.add_edge("B", "D")
graph.add_edge("B", "E")

graph.add_edge("C", "A")
graph.add_edge("C", "E")

graph.add_edge("D", "B")
graph.add_edge("D", "E")
graph.add_edge("D", "F")

graph.add_edge("E", "C")
graph.add_edge("E", "D")
graph.add_edge("E", "F")

graph.add_edge("F", "D")
graph.add_edge("F", "E")


# ============================================================
# 21. DISPLAY GRAPH
# ============================================================

print("\n\nGraph:")

graph.display_graph()


# ============================================================
# 22. REMOVE EDGE
# ============================================================

graph.remove_edge("A", "B")


# ============================================================
# 23. REMOVE VERTEX
# ============================================================

graph.remove_vertex("E")


# ============================================================
# 24. DISPLAY GRAPH AFTER DELETION
# ============================================================

print("\nGraph after removing edge A-B and vertex E:")

graph.display_graph()
