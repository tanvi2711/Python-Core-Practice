# **Magic Methods (Dunder Methods) - Short Notes**

## **What are Magic (Dunder) Methods?**

# * **Magic methods** are special methods in Python that have **double underscores (`__`)** before and after their names.
# * They are also called **Dunder Methods** (Double Underscore methods).
# * Python **automatically calls** these methods when performing certain operations on objects.
# * They allow us to define how objects behave.

# "Dunder" = Double Under ( __ )


## **Syntax**

# def __methodname__(self):
    # code


## **Common Magic Methods**

# | Magic Method | Purpose                                                        |
# | ------------ | -------------------------------------------------------------- |
# | `__init__()` | Constructor (called when an object is created)                 |
# | `__str__()`  | Returns a user-friendly string representation of an object     |
# | `__repr__()` | Returns an official string representation (used for debugging) |
# | `__len__()`  | Returns the length of an object                                |
# | `__add__()`  | Defines behavior of the `+` operator                           |
# | `__eq__()`   | Defines behavior of the `==` operator                          |


## **Example**

class Student:

    # Magic method (Constructor)
    def __init__(self, name):
        self.name = name

# Object creation automatically calls __init__()
s = Student("Tanvi")

print(s.name)

## **Why are they called Magic Methods?**

# Because **Python calls them automatically** behind the scenes.

# Example:

len([1, 2, 3])

# Python internally does:

[1, 2, 3].__len__()


## **Quick Points (Interview) ⭐**
# * Also called **Dunder (Double Underscore) Methods**.
# * Names start and end with `__`.
# * Invoked automatically by Python.
# * Used to customize the behavior of objects.
# * Example: `__init__()`, `__str__()`, `__len__()`, `__add__()`.