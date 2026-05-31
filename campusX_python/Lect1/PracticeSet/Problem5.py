# Q5:- Write a program to find the simple interest when the value of principle,rate of interest and time period is provided by the user.

principal=int(input("Enter principal : "))
rate=int(input("Enter rate : "))
time=int(input("Enter time : "))

simple_intrest=principal*rate*time/100

print("Simple Intrest = ",simple_intrest)