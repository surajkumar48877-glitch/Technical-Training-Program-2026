# ============================================================
# DAY 05 - PYTHON PRACTICE
# ============================================================


# ============================================================
# 1. CHECK STRING IS PALINDROME OR NOT
# ============================================================

name = "Suraj"

if name[:] == name[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# ============================================================
# 2. COUNT VOWELS AND CONSONANTS
# ============================================================

name = "HELP4code"
name = name.lower()

print(name)

vowel = 0
consonant = 0

for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vowel += 1
    elif i.isalpha():
        consonant += 1

print("Vowel =", vowel)
print("Consonant =", consonant)


# ============================================================
# 3. CHECK TWO STRINGS ARE ANAGRAMS OR NOT
# ============================================================

string1 = "silent"
string2 = "listen"

if sorted(string1) == sorted(string2):
    print("Anagrams")
else:
    print("Not Anagrams")


# ============================================================
# 4. COUNT WORDS IN A STRING
# ============================================================

var = "This is a sentence"

words = var.split()

print("Number of words =", len(words))


# ============================================================
# 5. REVERSE WORDS IN A STRING
# ============================================================

var = "Hello world"

words = var.split()
reverse_words = words[::-1]

print(" ".join(reverse_words))


# ============================================================
# 6. COUNT SPECIAL CHARACTERS
# ============================================================

text = "gasgg54@#vscsd!s*"

special_count = 0

for char in text:
    if not char.isalnum():
        special_count += 1

print("Special characters =", special_count)


# ============================================================
# 7. CHECK STRING IS TITLE CASE OR NOT
# ============================================================

name = "this is a test"

if name.istitle():
    print("String is in title case")
else:
    print("String is not in title case")


# ============================================================
# 8. DICTIONARY - DUPLICATE KEY
# ============================================================

student = {
    101: "suraj",
    102: "akash",
    "101": "ayush",
    101: "ram"
}

print(student)


# ============================================================
# 9. PRINT DICTIONARY KEYS
# ============================================================

student = {
    101: "suraj",
    102: "akash",
    "101": "ayush",
    101: "ram",
    "empname": "anish"
}

for i in student:
    print(i)


# ============================================================
# 10. PRINT DICTIONARY KEYS USING keys()
# ============================================================

for i in student.keys():
    print(i)


# ============================================================
# 11. PRINT DICTIONARY VALUES
# ============================================================

for i in student.values():
    print(i)


# ============================================================
# 12. PRINT DICTIONARY ITEMS
# ============================================================

for i in student.items():
    print(i)


# ============================================================
# 13. REMOVE ELEMENT USING pop()
# ============================================================

student = {
    101: "suraj",
    102: "akash",
    "101": "ayush",
    101: "ram",
    "empname": "anish"
}

student.pop(101)

print(student)


# ============================================================
# 14. CLEAR DICTIONARY
# ============================================================

student = {
    101: "suraj",
    102: "akash",
    "101": "ayush",
    101: "ram",
    "empname": "anish"
}

student.clear()

print(student)


# ============================================================
# 15. COPY DICTIONARY
# ============================================================

student = {
    101: "suraj",
    102: "akash",
    "101": "ayush",
    101: "ram",
    "empname": "anish"
}

newstudent = student.copy()

print(student)
print(newstudent)


# ============================================================
# 16. ACCESS VALUE FROM COPIED DICTIONARY
# ============================================================

print(newstudent[101])


# ============================================================
# 17. ADD NEW KEY-VALUE PAIR
# ============================================================

student = {
    101: "suraj",
    102: "akash",
    "101": "ayush",
    101: "ram",
    "empname": "anish"
}

student[103] = "DIP101"

print(student)


# ============================================================
# 18. STUDENT MARKS DICTIONARY
# ============================================================

n = int(input("Enter the number of students: "))

d = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    d[name] = marks

while True:
    name = input("Enter student name to get marks: ")

    marks = d.get(name, -1)

    if marks == -1:
        print("Student not found")
    else:
        print("The marks of", name, "is:", marks)

    option = input(
        "Do you want to find another student marks [yes/no]: "
    )

    if option.lower() == "no":
        break

print("Thanks for using our application")


# ============================================================
# 19. TUPLE AS DICTIONARY KEY
# ============================================================

a = {
    (1, 2): 1,
    (2, 3): 2,
    (4, 5): 3
}

print(a[4, 5])

# Reason:
# (4, 5) is a tuple key in the dictionary.


# ============================================================
# 20. MULTIPLE KEYS IN DICTIONARY ACCESS
# ============================================================

a = {
    "a": 1,
    "b": 2,
    "c": 3
}

# print(a["a", "b"])

# Reason:
# ("a", "b") is treated as a tuple key.
# This key does not exist in the dictionary,
# so it gives KeyError.


# ============================================================
# 21. COUNT FRUITS USING DICTIONARY
# ============================================================

fruit = {}


def addone(index):
    if index in fruit:
        fruit[index] += 1
    else:
        fruit[index] = 1


addone("apple")
addone("banana")
addone("Apple")

print(len(fruit))
print(fruit)


# ============================================================
# 22. INTEGER AND STRING KEYS
# ============================================================

arr = {}

arr[1] = 1
arr["1"] = 2
arr[1] += 1

print(arr)

total = 0

for k in arr:
    total += arr[k]

print("Sum =", total)

# Reason:
# 1 and "1" are different dictionary keys.


# ============================================================
# 23. INTEGER AND FLOAT KEYS
# ============================================================

arr = {}

arr[1] = 1
arr["1"] = 2
arr[1.0] = 4

print(arr)

total = 0

for k in arr:
    total += arr[k]

print("Sum =", total)

# Reason:
# 1 and 1.0 are treated as the same dictionary key.


# ============================================================
# 24. DIFFERENT FLOAT KEY
# ============================================================

arr = {}

arr[1] = 1
arr["1"] = 2
arr[1.1] = 4

print(arr)

total = 0

for k in arr:
    total += arr[k]

print("Sum =", total)


# ============================================================
# 25. TUPLE KEYS IN DICTIONARY
# ============================================================

my_dict = {}

my_dict[(1, 2, 4)] = 8
my_dict[(4, 2, 1)] = 10
my_dict[(1, 2)] = 12

total = 0

for k in my_dict:
    total += my_dict[k]

print("Sum =", total)
print(my_dict)


# ============================================================
# 26. NESTED DICTIONARY
# ============================================================

box = {}
jars = {}
creates = {}

box["biscuit"] = 1
box["cake"] = 3

jars["jam"] = 4

creates["jars"] = jars

print(creates)
print(len(creates["jars"]))


# ============================================================
# 27. SORT DICTIONARY KEYS
# ============================================================

data = {
    "c": 97,
    "a": 96,
    "b": 98
}

for key in sorted(data):
    print(data[key])


# ============================================================
# 28. QUEUE IMPLEMENTATION USING LIST
# ============================================================

class Queue:

    def __init__(self, queue_size):
        self.queue_size = queue_size
        self.queue_list = []

    # Check queue is full
    def is_full(self):
        if len(self.queue_list) == self.queue_size:
            return True
        else:
            return False

    # Check queue is empty
    def is_empty(self):
        if self.queue_list == []:
            return True
        else:
            return False

    # Add element
    def enqueue(self, value):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue_list.append(value)
            print(value, "added to queue")

    # Remove first element
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue_list.pop(0), "removed from queue")

    # Show first element
    def peek_front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element =", self.queue_list[0])

    # Delete queue
    def delete_queue(self):
        self.queue_list.clear()
        print("Queue has been deleted")

    # Display queue
    def display_queue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue =", self.queue_list)


# ============================================================
# QUEUE MENU
# ============================================================

size = int(input("Enter the size of queue: "))

queue_object = Queue(size)

while True:

    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek Front")
    print("4. Delete Queue")
    print("5. Display Queue")
    print("6. Is Empty")
    print("7. Is Full")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter the value to enqueue: "))
        queue_object.enqueue(value)

    elif choice == 2:

        queue_object.dequeue()

    elif choice == 3:

        queue_object.peek_front()

    elif choice == 4:

        queue_object.delete_queue()

    elif choice == 5:

        queue_object.display_queue()

    elif choice == 6:

        print("Queue is empty:", queue_object.is_empty())

    elif choice == 7:

        print("Queue is full:", queue_object.is_full())

    elif choice == 8:

        print("Exit")
        break

    else:

        print("Invalid input")
