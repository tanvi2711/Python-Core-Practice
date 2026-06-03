# Problem 9: Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.


sum=0
count=0
while True:   # for infinite loop
    num=int(input())
    if num==0:
        break
    sum=sum+num
    count+=1
avg=sum/count
print("Sum= ",sum)
print("Average= ",avg)