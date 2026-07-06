n=int(input("Enter number: "))

c=0

for i in range(1,n+1):
    c+=i**3

print(c)

print(((n*(n+1))//2)**2)