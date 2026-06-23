# Q4: find union of n arrays.

# Input:
# [[1, 2, 2, 4, 3, 6],
#  [5, 1, 3, 4],
#  [9, 5, 7, 1],
#  [2, 4, 1, 3]]


# Output:
# [1, 2, 3, 4, 5, 6, 7, 9]


l=[[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]

l1=[]

print(list(((set(l[0])|set(l[1]))|set(l[2]))|set(l[3])))



u = set()

for i in l:
    u = u | set(i)

print(list(u))