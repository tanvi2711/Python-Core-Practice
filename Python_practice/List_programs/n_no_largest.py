# Given a list of integers, the task is to find the N largest elements from it, assuming the list contains at least N elements.

# Example:

# Input: [4, 5, 1, 2, 9] 
#         N = 2
# Output: [9, 5]

a=[4, 5, 1, 2, 9] 
N = 2


for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]

for i in range(N):
    print(a[i])
