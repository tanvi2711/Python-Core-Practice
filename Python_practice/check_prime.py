n=int(input("Enter number: "))
f=0

for i in range(2,n+1):
    f=0
    for j in range(2,i):
        if i%j==0:
            f=1
if f==1:
        print(f"{i} not is prime")   
else:
    print(f"{i} is prime")
