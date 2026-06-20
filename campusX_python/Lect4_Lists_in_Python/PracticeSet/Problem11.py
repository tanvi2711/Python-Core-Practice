# ### `Problem 11:` Write a program that can perform union operation on 2 lists

# **Example:**

# Input:

# [1,2,3,4,5,1]
# [2,3,5,7,8]


# Output:
# [1,2,3,4,5,7,8]


n1=[1,2,3,4,5,1]
n2=[2,3,5,7,8]

c=[]

for i in n1:  
    if i not in c:
        c.append(i)

for j in n2:
    if j not in c:
        c.append(j)

c.sort()        
print(c)
