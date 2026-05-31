# Q7:- Write a program to find the sum of squares of first n natural numbers where n will be provided by the user.

n=int(input("Enter any no: "))

sum=0
for i in range(1,n+1):
    sum=sum+(i*i)
print("sum of squares of first n natural numbers is :",sum)

