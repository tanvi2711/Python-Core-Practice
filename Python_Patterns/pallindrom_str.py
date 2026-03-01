# Check if number is palindrome (121 → True)


num=int(input("Enter any no: "))
rev=0
while(num>0):
    rev=(rev*10)+num%10	
    num=num//10

if rev==num:
    print("It is pallindrom number")
