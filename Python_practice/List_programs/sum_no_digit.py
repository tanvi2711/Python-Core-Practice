# Given a list of integers, write a Python program to calculate the sum of digits for each element and store the results in a new list. For Example:

# Input: [123, 456, 789]  
# Output: [6, 15, 24]
# Explanation:  123 = 1 + 2 + 3 = 6  
#                         456 = 4 + 5 + 6 = 15  
#                         789 = 7 + 8 + 9 = 24  

a=[123, 456, 789]  

l=[]


for i in a:
    s=0
    while i!=0:
        r=i%10
        s+=r
        i=i//10
    l.append(s)
print(l)