# Problem 10: Write a program that will take 2 numbers as input and prints the LCM and HCF of those 2 numbers

import math

num1=int(input("Enter any no : " ))
num2=int(input("Enter any no : " ))

hcf=math.gcd(num1,num2)
lcm=math.lcm(num1,num2)

print("LCM: ",lcm," HCF: " ,hcf)