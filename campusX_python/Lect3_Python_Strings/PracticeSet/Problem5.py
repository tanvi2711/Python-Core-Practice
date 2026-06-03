# Problem 5: Write a Python Program to Find the Sum of the Series till the nth term: 
# 1 + x^2/2 + x^3/3 + … x^n/n
# n will be provided by the user


n=int(input("Enter value of n: " ))
x=int(input("Enter value of x:"))

sum=1
for i in range (2,n+1):
    sum=sum+(x**i/i)
print("Sum:" , sum)