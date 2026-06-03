# Problem 9: Write a program that will take a decimal number as input and prints out the binary equivalent of the number

num=int(input("Enter any decimal no: "))
binary=0
i=1
while(num!=0):
    rem=num%2
    binary=binary+rem*i
    num=num//2
    i*=10
print("Binary: ",binary)