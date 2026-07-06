# Given two integers, start and end, the task is to print all positive numbers between the given range, including both endpoints. For Examples:

# Input: start = -5, end = 3  
# Output: [1, 2, 3]


a=[]
for i in range(-5,4):
    if i>0:
        a.append(i)

print(a)