# Given a list of numbers, the task is to find the cumulative sum (also known as the running total) where each element in the output represents the sum of all elements up to that position in the original list.

# Example:

# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]

a=[1, 2, 3, 4]

l=[]
s=0
for i in a:
    s+=i
    l.append(s)

print(l)