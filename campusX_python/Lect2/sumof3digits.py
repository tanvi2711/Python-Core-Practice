# Program - Find the sum of a 3 digit number entered by the user

num=int(input("Enter any 3 digit no: "))

a=num%10
num=num//10
b=num%10
num=num//10
c=num%10

print("sum of a 3 digit number: " ,a+b+c)