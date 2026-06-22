# Functions are 1st class citizens

# First-Class Citizen

# An object that can:

# Be assigned to a variable
# Be passed as an argument
# Be returned from a function
# Be stored in data structures
# Functions as First-Class Citizens

# In Python, functions are first-class citizens because they can:

# Be assigned to variables
# Be passed to other functions
# Be returned from functions
# Be stored in lists, tuples, and dictionaries


# Benefits
# Enables higher-order functions
# Supports callbacks
# Makes code more flexible and reusable
# Used in decorators and functional programming

# In Python: Integers, strings, lists, tuples, dictionaries, classes, and functions are all first-class citizens. Functions are commonly highlighted because many advanced Python features depend on this capability.




# ==========================================
# FUNCTIONS ARE FIRST-CLASS CITIZENS
# ==========================================

# In Python, functions are treated like
# any other object (int, string, list, etc.)

# This means functions can:
# 1. Have a type and id
# 2. Be assigned to variables
# 3. Be deleted
# 4. Be stored in data structures
# 5. Be passed as arguments
# 6. Be returned from other functions

print("===================type n id=======================")
# type n id 
def sqr(num):
    return num**2

print(type(sqr))
print(id(sqr))


a=2
print(type(a))
print(id(a))



print("===================reassign=======================")
# reassign 
x=sqr
print(x)  
print(id(x))
print(x(3))


# deleting a function
# del sqr
# sqr(3) # not work function is deleted


print("====================storing======================")
# storing
l=[1,2,3,4,5,sqr]
print(l)
print(l[-1](3))



print("================fuction is a immutable datatype==========================")
# fuction is a immutable datatype
s={sqr}  # sets can only allow immutable datatypes
print(s)



print("===================RETURNING A FUNCTION=======================")
# RETURNING A FUNCTION
def outer():

    def inner():
        print("Hello from Inner Function")

    return inner

func = outer()

func()

# Output:
# Hello from Inner Function



print("================function as argument==========================")
# function as argument

def func_a():
    print('inside func_a')  # Prints a message when func_a is called

def func_b(z):
    print('inside func_c')  # Prints a message first

    # z contains a function reference (func_a in this case)
    # z() calls that function
    return z()


# Passing func_a as an argument to func_b
# Note: func_a is passed WITHOUT parentheses,
# so only its reference is passed, not executed yet.
print(func_b(func_a))