# ==========================================
# Constructor and Object Creation
# ==========================================

class Atm:

    # Constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0

# Creating an object
obj = Atm()

# Accessing instance variables
print(obj.pin)
print(obj.balance)

# Output:
#
# 0


# ### Explanation:

# * `class Atm:` → Creates a class named **Atm**.
# * `__init__()` → Constructor that is called automatically when an object is created.
# * `self.pin = ''` → Initializes the `pin` instance variable with an empty string.
# * `self.balance = 0` → Initializes the `balance` instance variable with `0`.
# * `obj = Atm()` → Creates an object of the `Atm` class. The constructor is called automatically.
# * `print(obj.pin)` and `print(obj.balance)` → Access the object's instance variables.

### Key Points:

# * `__init__()` is the constructor in Python.
# * `self` refers to the current object.
# * Instance variables are created using `self`.
# * The constructor is executed automatically whenever an object is created.
# * Every object has its own copy of instance variables.

### Syntax:

class ClassName:
    def __init__(self):
        self.variable = 'value'

obj = ClassName()


### Memory Trick:

# * **Class** → Blueprint
# * **Object** → Real instance created from the blueprint
# * **`__init__()`** → Initializes the object
# * **`self`** → Refers to the current object

### Interview Question:

# **Q. How do you create an object in Python?**
# **Answer:** By calling the class name with parentheses.

obj = ClassName()


# **Q. When is `__init__()` called?**
# **Answer:** It is called automatically whenever an object of the class is created.




# ========================= CONSTRUCTOR (__init__) =========================

# What is a Constructor?
# - A constructor is a special (magic/dunder) method named __init__().
# - It is automatically called whenever an object is created.

# Why is it used?
# - To initialize (assign) the initial values of object attributes.
# - Saves time by avoiding manual initialization.
# - Makes code clean, readable, and less error-prone.
# - Ensures every object starts with default or required values.

# Syntax:
# class ClassName:
#     def __init__(self):
#         # initialization code

# Example:
class Atm:

    # Constructor
    def __init__(self):
        self.pin = ""      # Default PIN
        self.balance = 0   # Default balance

# Object creation
obj = Atm()    # __init__() is called automatically

print(obj.pin)      # Output:
print(obj.balance)  # Output: 0


# Constructor (__init__) is a special method that is automatically called
# when an object is created. It is used to initialize object attributes.


# for ex any application we have diff functionality if it has constructor it will consisits configuration of that application a work which is not dependent on customer its a host job is written in that constructor
#    ex god is programmer class is  earth  objects are humans then constructor is death n birth which is not in hands of human 