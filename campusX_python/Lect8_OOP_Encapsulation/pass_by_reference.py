# ============================================================
# PASS BY OBJECT REFERENCE IN PYTHON
# ============================================================

class Person:

    # Parameterized Constructor
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# Function outside the class
def greet(person):

    # 'person' receives the SAME object reference as 'p'
    # No new object is created here.
    print(id(person))      # Address of person object

    print("Hi my name is", person.name, "and I am a", person.gender)

    # Creating a NEW object
    p1 = Person("ankit", "male")

    # Returning the reference of the new object
    return p1


# Creating an object
p = Person("Tanvi", "Female")

# Passing object 'p' to greet()
# 'person' and 'p' point to the SAME object.
x = greet(p)

# Same address as 'person'
print(id(p))

# x stores the reference of the NEW object (p1)
print(x.name)
print(x.gender)


# Output Concept:
#
# p --------------------+
#                       |
# person ---------------+------> Person("Tanvi", "Female")
#
# x ----------------------------> Person("ankit", "male")
#
# Therefore:
# id(person) == id(p)
# But x points to a different object.


print("||||||||||||||||||||||||||||||||||")


# ============================================================
# OBJECT MUTABILITY
# ============================================================

# Objects are MUTABLE.
# This means if we change an object's attributes inside a function,
# the changes are reflected outside the function because both
# variables point to the SAME object.

class Person:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# Function outside the class
def greet(person):

    # Modifying the object's attribute
    # No new object is created.
    person.name = "ankit"

    # Returning the SAME object
    return person


# Creating object
p = Person("nitish", "male")

# Address of original object
print(id(p))

# Passing object reference
p1 = greet(p)

# Address remains the SAME because greet()
# returned the original object.
print(id(p1))

# Verify that the object was modified
print(p.name)      # ankit
print(p1.name)     # ankit


# Memory Representation:
#
# Before greet():
#
# p  ---------------------> Person(name="nitish", gender="male")
#
#
# Inside greet():
#
# person -----------------> Same Person Object
#
# person.name = "ankit"
#
#
# After greet():
#
# p  ---------------------> Person(name="ankit", gender="male")
# p1 ----------------------> Same Person Object
#
# Therefore:
# id(p) == id(person) == id(p1)
#
# Only ONE object exists in memory.
# Multiple variables (p, person, p1) point to that same object.