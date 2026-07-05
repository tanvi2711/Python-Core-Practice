n=int(input("Enter number: "))

s=0

for i in range(1,n+1):
    s+=i**2

print(s)

import functools

x=functools.reduce(lambda x,y: x+y**2 ,range(1,n+1))
print(x)