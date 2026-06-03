# Problem 13:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.


num=int(input("Enter any no: "))

sum=0
arm=num

while(num!=0):
    digit=num%10
    sum=sum+(digit**3)
    num=num//10

if sum==arm:
    print(arm,"is Armstrong number ")
else:
    print(arm,"is not Armstrong number ")