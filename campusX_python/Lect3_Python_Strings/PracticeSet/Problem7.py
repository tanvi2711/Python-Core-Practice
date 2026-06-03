# Problem 7 - Find the sum of the series upto n terms.
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690. Take the user input and then calculate. And the output style should match which is given in the example.

# Example 1:

# Input:

# 5
# Output:

# 2+22+222+2222+22222
# Sum of above series is: 24690


num=int(input("Enter any no: "))

m=' '
sum=0
for i in range(1,num+1):
    m='2'*i
    sum=sum+int(m)
print(sum)


# Different logic
# m=0
# sum=0
# for i in range(1,num+1):
#     m=m*10+2
#     sum=sum+int(m)
#     print(m,sum)
# print(sum)