# ==========================================
# self in Python
# ==========================================

# What is self?
# - 'self' is a reference to the CURRENT OBJECT of a class.
# - It allows an object to access its own variables (attributes)
#   and methods.

# Why is self used?
# - To differentiate object variables from local variables.
# - To access and modify object data.
# - To call one method from another method within the same class.

# Important Points
# 1. 'self' is NOT a keyword in Python.
# 2. It is just a naming convention (you can use any name,
#    but 'self' is the standard and should always be used).
# 3. Python automatically passes the current object as the
#    first argument when a method is called.

# Syntax:
# class ClassName:
#     def method(self):
#         pass

# Example:
class Student:

    def __init__(self, name):
        self.name = name      # Object variable

    def display(self):
        print(self.name)      # Accessing object variable


s1 = Student("Tanvi")
s1.display()

# Internally, Python does this:
# Student.display(s1)

# Here,
# self = s1

# Memory Representation
# s1 ─────────► Student Object
#                 |
#                 └── name = "Tanvi"

# Common Uses of self
# ✔ Access object variables
# ✔ Modify object variables
# ✔ Call another method of the same class
# ✔ Pass the current object to another function/method

# Example of calling another method
class Demo:

    def greet(self):
        print("Hello")

    def show(self):
        self.greet()      # Calling another method using self

d = Demo()
d.show()

# Difference: Local Variable vs Object Variable

# Local Variable
def example():
    x = 10          # Exists only inside this function

# Object Variable
class Test:
    def __init__(self):
        self.x = 10 # Belongs to the object and can be
                    # accessed by all methods of the class


# Interview Points
# ✔ self refers to the current object.
# ✔ It is the first parameter of every instance method.
# ✔ It is passed automatically by Python.
# ✔ It is used to access instance variables and methods.
# ✔ It is not a keyword, only a naming convention.


class Atm:

    # Constructor
    def __init__(self):
        print(id(self))
        self.pin = ''
        self.balance = 0

# Creating an object
obj = Atm()

print(id(obj))




# ==========================================

# Why does `self` have the same address as the object?

# ==========================================

## Answer

# `self` has the **same memory address** as the object because `self` is simply another reference to that object.

# When we create an object:

s1 = Student()


# `s1` stores the address of the `Student` object.

# When we call a method:

s1.display()

# Python **automatically** converts it into:

Student.display(s1)


# Here, the object `s1` is passed as the first argument to the method.

# So inside the method:

self = s1

# This means both `self` and `s1` refer to the **same object**, therefore they have the **same memory address**.

# ### Memory Representation

#           +----------------------+
# s1 ------>|    Student Object    |
# self ---->|                      |
#           +----------------------+
# ```

# Both `s1` and `self` point to the **same object**, so printing them gives the same address.

### Example

class Student:

    def display(self):
        print(self)

s1 = Student()

print(s1)
s1.display()


# Both addresses are the same because **`self` is another reference to the object (`s1`) that called the method.**

# ### One-Line Interview Answer

# self` and the object (e.g., `s1`) have the same address because Python automatically passes the calling object as the first argument to the method, so internally `self = s1`.**


# in java self is call 'THIS'

# class ke andar ki variable n methods ek dusare se directly baat nahi kr skte thats why we used self 