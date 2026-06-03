# Problem 6: The natural logarithm can be approximated by the following series.

# (x-1)/x + (1/2)*((x-1)/x)^2 + (1/3)*((x-1)/x)^3 +..........

# If x is input through the keyboard, write a program to calculate the sum of the first seven terms of this series.


x=int(input("Enter value of x: "))

sum=0

for i in range(1,8):
    sum=sum+(1/i*((x-1)/x)**i)
print("Sum: ",sum)