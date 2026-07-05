def simple_intrest(p,n,r):
    return (p*n*r)/100

p=int(input("Enter principal amount: "))
n=int(input("Enter no of years: "))
r=int(input("Enter rate of intrest: "))

print(simple_intrest(p,n,r))

x=lambda p,n,r: (p*n*r)/100

print(x(p,n,r))

x=[(p*n*r)/100][0]
print(x)