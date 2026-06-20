# Problem 4:Running Sum on list
# Write a program to print a list after performing running sum on it.

# i.e:
# Input:
# list1 = [1,2,3,4,5,6]

# Output:
# [1,3,6,10,15,21]

list1 = [1,2,3,4,5,6]

sum=0
l1=[]

for i in list1:
    sum=sum+i
    l1.append(sum)
print(l1)


for i in range(1,len(list1)):
    list1[i]+=list1[i-1]

print(list1)
