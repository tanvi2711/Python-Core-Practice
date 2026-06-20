# Problem 12:` Write a program that can find the max number of each row of a matrix

# **Example:**

# Input:
# [[1,2,3],[4,5,6],[7,8,9]]


# Output:
# [3,6,9]

l=[[1,2,3],[4,5,6],[7,8,9]]

l1=[]

for i in l:
    l1.append(i[2])
print(l1)