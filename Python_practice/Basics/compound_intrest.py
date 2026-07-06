p=int(input("Enter principal amount: "))
n=int(input("Enter no of years: "))
r=int(input("Enter rate of intrest: "))


# calculate amount
a=p*(1+r/100)**n 
cp=a-p

print(cp)

a=p*pow((1+r/100),n)
cp=a-p

print(cp)


a=p
for i in range(1,r+1):
    a=a*(1+r/100)
cp=a-p

print(cp)
