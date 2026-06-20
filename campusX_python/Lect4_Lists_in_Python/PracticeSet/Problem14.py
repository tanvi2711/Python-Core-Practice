# `Problem 14:` Write a list comprehension that can transpose a given matrix

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]


for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[j][i],end=" ")
    print() 


l1=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]

print(l1)

