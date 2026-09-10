# ============================================================
# DAY 09 - PYTHON PRACTICE
# Topics:
# List Comprehension, Dictionary Comprehension,
# Multiple Inputs, String Methods, Unique Vowels,
# Adjacency Matrix
# ============================================================


# ============================================================
# 1. LIST COMPREHENSION
# ============================================================

# Square of numbers from 1 to 10
s = [i * i for i in range(1, 11)]
print("Squares:", s)


# Power of 2
val = [2 ** i for i in range(1, 6)]
print("Powers of 2:", val)


# Even values from the list
val2 = [i for i in s if i % 2 == 0]
print("Even squares:", val2)


# ============================================================
# 2. DICTIONARY COMPREHENSION
# ============================================================

# Dictionary of squares
squares = {x: x * x for x in range(1, 6)}
print("Squares Dictionary:", squares)


# Dictionary of doubles
doubles = {x: 2 * x for x in range(1, 6)}
print("Doubles Dictionary:", doubles)


# ============================================================
# 3. READING MULTIPLE INTEGER VALUES
# ============================================================

a, b = [int(x) for x in input("\nEnter 2 numbers: ").split()]
print("Product is:", a * b)


# ============================================================
# 4. READING MULTIPLE FLOAT VALUES
# ============================================================

a, b, c = [
    float(x) for x in input("Enter 3 float numbers: ").split(",")
]

print("The sum is:", a + b + c)


# ============================================================
# 5. REMOVING SPACES FROM STRING
# ============================================================

city = input("\nEnter your city name: ")

print("Using rstrip():", city.rstrip())
print("Using lstrip():", city.lstrip())
print("Using strip():", city.strip())


# ============================================================
# 6. CITY NAME CHECK
# ============================================================

scity = city.strip().lower()

if scity == "hyderabad":
    print("Hello Hyderabadi... Adaab!")
elif scity == "chennai":
    print("Hello Chennai... Vanakkam!")
elif scity == "bangalore":
    print("Hello Kannadiga... Subha!")
else:
    print("You entered a wrong city")


# ============================================================
# 7. REPLACE STRING
# ============================================================

s = "Python is difficult"
s1 = s.replace("difficult", "easy")

print("\nAfter replacement:", s1)


# Replace all occurrences
s = "abbbabab"
s1 = s.replace("a", "b")

print("After replacing all 'a' with 'b':", s1)


# ============================================================
# 8. FIND UNIQUE VOWELS FROM A WORD
# ============================================================

vowels = ['a', 'e', 'i', 'o', 'u']

word = input(
    "\nEnter the word where we will search the vowels: "
).lower()

found = []

for character in word:
    if character in vowels:
        if character not in found:
            found.append(character)

print("Found vowels =", found)
print("Unique vowels =", len(found), "from the given word =", word)


# ============================================================
# 9. STATIC ADJACENCY MATRIX
# ============================================================

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices

        # Create adjacency matrix
        self.matrix = [
            [0] * vertices for _ in range(vertices)
        ]

    def display(self):
        print("\nAdjacency Matrix:")

        for row in self.matrix:
            print(*row)

    def add_edge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 1


# Create graph with 5 vertices
graph = Graph(5)

# Add edges
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)

graph.add_edge(1, 0)
graph.add_edge(1, 4)

graph.add_edge(2, 0)
graph.add_edge(2, 3)

graph.add_edge(3, 0)
graph.add_edge(3, 4)
graph.add_edge(3, 2)

graph.add_edge(4, 1)
graph.add_edge(4, 3)

graph.display()


# ============================================================
# 10. DYNAMIC ADJACENCY MATRIX
# ============================================================

class DynamicGraph:
    def __init__(self, vertices):
        self.vertices = vertices

        # Create adjacency matrix
        self.matrix = [
            [0] * vertices for _ in range(vertices)
        ]

    def display(self):
        print("\nDynamic Adjacency Matrix:")

        for row in self.matrix:
            print(*row)

    def add_edge(self, vertex1, vertex2):
        self.matrix[vertex1][vertex2] = 1


# Take number of vertices from user
n = int(input("\nEnter the number of vertices: "))

graph = DynamicGraph(n)

# Take number of edges from user
edges = int(input("Enter the number of edges: "))

# Take edges from user
for i in range(edges):
    v1, v2 = map(
        int,
        input("Enter edge (v1 v2): ").split()
    )

    graph.add_edge(v1, v2)

graph.display()
