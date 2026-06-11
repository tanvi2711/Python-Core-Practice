# Deleting items from a List
print("----------Deleting items from a List----------")

l=[1,2,3,4,5,6]


# del
# del l
# indexing
del l[-1]
print(l)

del l[3]
print(l)

# slicing
del l[1:3]
print(l)


# remove
l=[1,2,3,4,5,6]
l.remove(2)    # it will delete exact no means we dont have to tell index here
l.remove(5)
print(l)

# pop
l=[1,2,3,4,5,6]
l.pop()  # it will delete last element or particular element
l.pop(0)  #index
print(l)

# clear
l=[1,2,3,4,5,6]
l.clear()
print(l)

