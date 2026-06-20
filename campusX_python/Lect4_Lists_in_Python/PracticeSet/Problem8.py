# `Problem 8:` Split String of list on K character.

# **Example :**

# Input:
# ['CampusX is a channel', 'for data-science', 'aspirants.']

# Output:
# ['CampusX', 'is', 'a', 'channel', 'for', 'data-science', 'aspirants.']


l=['CampusX is a channel', 'for data-science', 'aspirants.']

l1=[]

for i in l:
    w=i.split()
    for j in w:
        l1.append(j)
print(l1)



l1=[j for i in l for j in i.split() ]

print(l1)