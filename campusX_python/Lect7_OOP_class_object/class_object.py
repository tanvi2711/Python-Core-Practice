# ==========================================
# Creating an Object in Python
# ==========================================

# Definition:
# An object is an instance of a class.
# It is created using the class name followed by parentheses ().

# Syntax:
# object_name = ClassName()

# Example:

class Student:
    pass

# Creating objects
s1 = Student()
s2 = Student()

print(s1)
print(s2)

# Output:
# <__main__.Student object at 0x...>
# <__main__.Student object at 0x...>

# Explanation:
# 1. Student is a class.
# 2. s1 = Student() creates the first object.
# 3. s2 = Student() creates the second object.
# 4. Each object has a different memory location.

# Key Points:
# • Object is an instance of a class.
# • Multiple objects can be created from the same class.
# • Every object has its own memory location.
# • Objects are used to access the class's variables and methods.


l=[1,2,3,4,5]
print(type(l))


l=list()   #here l is a object of list class

s='hello'
print(type(s))