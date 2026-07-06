# Given a list of integers, the task is to identify and print all elements that appear more than once in the list. 
# For Example: I
# Input: [1, 2, 3, 1, 2, 4, 5, 6, 5]
# Output: [1, 2, 5]. 

a=[1, 2, 3, 1, 2, 4, 5, 6, 5]

l=[]

for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            l.append(a[j])
print(l)