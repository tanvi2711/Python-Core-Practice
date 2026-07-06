# Given a list of numbers, the task is to find the second largest element in that list.

# For example:

# li = [10, 20, 4, 45, 99] -> Second largest number = 45
# li = [5, 8, 12, 3, 7] -> Second largest number = 8



# a = [10, 20, 4, 45, 99]
a=[5, 8, 12, 3, 7]


# sort
for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
            

print("Second largest: ",a[len(a)-2])

