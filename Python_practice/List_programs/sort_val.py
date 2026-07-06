# Given two lists of equal length, where the second list defines the order, the task is to reorder the first list according to the sorted order of the second list.

# Example:

# Input:
# List A (to sort): ['x', 'y', 'z', 'w']
# List B (order list): [40, 10, 30, 20]

# Output:
# ['y', 'w', 'z', 'x']


a=['x', 'y', 'z', 'w']
b=[40, 10, 30, 20]

d={}

n=10

for i,j in zip(range(len(a)),range(len(b))):
    d[a[i]]=n
    n+=10
print(d)

c=[]
for i in b:
    if i in d.values():
        j=d[i]
        c.append(j)

print(c)