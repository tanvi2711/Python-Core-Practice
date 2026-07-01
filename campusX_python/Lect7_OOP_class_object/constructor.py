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
