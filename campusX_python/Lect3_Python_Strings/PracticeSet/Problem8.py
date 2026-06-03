# Problem 8`: Write a program to print all the unique combinations of 1,2,3 and 4 

# Output:
# 1 2 3 4
# 1 2 4 3
# 1 3 2 4
# 1 3 4 2
# 1 4 2 3
# 1 4 3 2
# 2 1 3 4
# 2 1 4 3
# 2 3 1 4
# 2 3 4 1
# 2 4 1 3
# .
# .
# and so on


for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        if j!=i:
            for k in [1,2,3,4]:
                if k!=i and k!=j:
                    for l in [1,2,3,4]:
                       if l!=i and l!=j and l!=k:
                          for m in [1,2,3,4]:
                              print([i,j,k,l])