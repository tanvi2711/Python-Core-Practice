# 1. Lists
# What are Lists?
# Lists Vs Arrays
# Characterstics of a List
# How to create a list
# Access items from a List
# Editing items in a List
# Deleting items from a List
# Operations on Lists
# Functions on Lists


# What are Lists
# List is a data type where you can store multiple items under 1 name. More technically, lists act like dynamic arrays which means you can add more items on the fly.

#In list we can store multiple datatypes
l=[20,'jessica',76.89,[1,2,3]]   



# Array Vs Lists
# Fixed Vs Dynamic Size
    # we have to declare size of array while creation of arrays
    # where as in list we can add infinite no of elements on the go list does not have a fix size (dynamic arrays=we can add more elements with out limit) list is flexible
# Convenience -> Hetrogeneous
    # arryas are homogeneus we can add one type of datatype into it
    # where as lists can stores multiple datatypes into it
# Speed of Execution
    # list execution speed is slow whereas arrays are fast
# Memory
    # list occupy more space in memory in compare to array


# a=2
# print(id(a)) #prints address of variable
 
li=[1,2,3]

print("List address: ",id(li))

print("--------Address of elements in list--------")
print(id(li[0]))
print(id(li[1]))
print(id(li[2]))

print("--------Address of elements--------")
print(id(1))
print(id(2))
print(id(3))