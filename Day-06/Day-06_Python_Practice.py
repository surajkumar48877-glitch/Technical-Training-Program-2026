# ============================================================
# DAY 06 - PYTHON PRACTICE
# ============================================================


# ============================================================
# 1. INSTANCE VARIABLE
# ============================================================

# Instance variables are those variables
# which depend on the object.


class Employee:

    def __init__(self):
        self.name = "Suraj"


obj1 = Employee()
obj2 = Employee()
obj3 = Employee()

print(obj1.name)
print(obj2.name)
print(obj3.name)

# Changing instance variable separately
obj1.name = "Kumar"
obj2.name = "Mishra"

print(obj1.name)
print(obj2.name)
print(obj3.name)


# ============================================================
# 2. ACCESSING AND DELETING INSTANCE VARIABLES
# ============================================================


class Student:

    def __init__(self):
        self.s_name = input("Enter your name: ")
        self.s_rollno = 101

    def get_data(self):
        self.s_mb = 3484893488


obj = Student()

# Creating instance variable using object
obj.get_data()

obj.s_branch = "CS"

# Deleting instance variable
del obj.s_rollno

print(obj.__dict__)


# ============================================================
# 3. STATIC VARIABLE
# ============================================================

# Static variables are those variables
# which do not depend on a particular object.


class College:

    college_name = "Sandip University"


obj1 = College()
obj2 = College()
obj3 = College()

print(obj1.college_name)
print(obj2.college_name)
print(obj3.college_name)


# Changing static variable using class
College.college_name = "Modern University"

print(obj1.college_name)
print(obj2.college_name)
print(obj3.college_name)


# ============================================================
# 4. INSTANCE VARIABLE AND STATIC VARIABLE TOGETHER
# ============================================================


class College:

    college_name = "Modern College"   # Static variable

    def __init__(self):
        self.student_name = "Suraj"   # Instance variable


principal = College()
teacher = College()
accountant = College()

print(principal.college_name, principal.student_name)
print("Teacher:", teacher.college_name, "...", teacher.student_name)
print("Accountant:", accountant.college_name, "...", accountant.student_name)


# Changing static variable
College.college_name = "HBD"

# Changing instance variable
principal.student_name = "Suraj Mishra"

print("Principal =", principal.college_name, "|", principal.student_name)
print("Teacher =", teacher.college_name, "|", teacher.student_name)
print("Accountant =", accountant.college_name, "|", accountant.student_name)


# ============================================================
# 5. CREATING INDEPENDENT NODES
# ============================================================


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


linked_obj = LinkedList()

# Creating independent nodes
linked_obj.head = Node(10)
second = Node(20)
third = Node(30)

# Connecting nodes
linked_obj.head.next = second
second.next = third

# Display linked list
current = linked_obj.head

while current != None:
    print("[", current.data, "] ->", end=" ")
    current = current.next

print("None")


# ============================================================
# 6. LINKED LIST WITH FOUR NODES
# ============================================================


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


linked_obj = LinkedList()

# Creating nodes
linked_obj.head = Node(10)
second = Node(20)
third = Node(30)
fourth = Node(40)

# Connecting nodes
linked_obj.head.next = second
second.next = third
third.next = fourth

# Display linked list
current = linked_obj.head

while current != None:
    print(
        "[", current.data, "|", current.next, "] ->",
        end=" "
    )
    current = current.next

print("None")


# ============================================================
# 7. ADD NODE AT BEGINNING
# ============================================================


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_beginning(self, value):

        node_value = Node(value)

        if self.head is None:
            self.head = node_value
            self.tail = node_value

        else:
            node_value.next = self.head
            self.head = node_value

    def display(self):

        current = self.head

        while current is not None:
            print("[", current.data, "] ->", end=" ")
            current = current.next

        print("None")


linked_obj = LinkedList()

linked_obj.add_node_beginning(10)
linked_obj.add_node_beginning(5)
linked_obj.add_node_beginning(2)

linked_obj.display()


# ============================================================
# 8. ADD NODE AT BEGINNING AND END
# ============================================================


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # Add node at beginning
    def add_node_beginning(self, value):

        node_value = Node(value)

        if self.head is None:
            self.head = node_value
            self.tail = node_value

        else:
            node_value.next = self.head
            self.head = node_value

    # Add node at end
    def add_node_end(self, value):

        node_value = Node(value)

        if self.head is None:
            self.head = node_value
            self.tail = node_value

        else:
            self.tail.next = node_value
            self.tail = node_value

    # Display linked list
    def display(self):

        current = self.head

        while current is not None:
            print("[", current.data, "] ->", end=" ")
            current = current.next

        print("None")


# Creating Linked List object
linked_obj = LinkedList()

# Adding nodes at beginning
linked_obj.add_node_beginning(10)
linked_obj.add_node_beginning(5)
linked_obj.add_node_beginning(2)

# Adding nodes at end
linked_obj.add_node_end(20)
linked_obj.add_node_end(30)

# Display
linked_obj.display()
