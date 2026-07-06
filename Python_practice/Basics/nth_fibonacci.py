n=int(input("Enter number: "))
m=int(input("Enter number: "))

a,b=0,1

for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    if c%m==0:
        print(c,end=" ")
