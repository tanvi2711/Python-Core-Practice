# Problem-12: Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
# Input:
# list1 = [1,2,3,4,5,6]

# Output:
# [1,2,9,64,625,-]


list1 = [1,2,3,4,5,6]

x=list(map(lambda x,y:x**y,list1,range(len(list1))))

print(x)