n=int(input("Enter number: "))

f=0
a,b=0,1

for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    if c==n:
        f=1

if f==1 or n==0:
    print(f"{n} is fiboncci number ")
else:
    print(f"{n} is not fiboncci number ")