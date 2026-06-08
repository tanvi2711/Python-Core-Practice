# Problem 13:Print all the Armstrong numbers in a given range.
# Range will be provided by the user
# Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.


num=int(input("Enter any no: "))

for i in range (0,num+1):
    sum=0
    arm=i

    while(arm!=0):
        digit=arm%10
        sum=sum+(digit**3)
        arm=arm//10

    if sum==i:
        print(i,end=" ")