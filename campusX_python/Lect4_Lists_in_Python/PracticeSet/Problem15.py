# Problem 15: Write a list comprehension that can flatten a nested list
# Input
# matrix = [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

# l=[]

# for i in matrix:
#     for j in i:
#         l.append(j)

# print(l)


l=[j for i in matrix for j in i]
print(l)