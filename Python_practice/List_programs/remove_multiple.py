# Given a list of numbers, the task is to remove multiple specified elements from it. Removing multiple elements means eliminating all occurrences of these elements and returning a new list with the remaining numbers.

# For example:

# a = [10, 20, 30, 40, 50, 60, 70]
# remove = [20, 40, 60]
# Resulting list = [10, 30, 50, 70

a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]

x=[i for i in a if i  not in remove]

print(list(x))

l=[]
for i in a:
    if i not in remove:
        l.append(i)
print(l)