l=[]
n=int(input("Enter range of list: "))
for i in range(n):
    i=int(input("Enter no: "))
    l.append(i)

s=0

for i in l:
    s+=i

print("Sum: ",s)

import functools 

x=functools.reduce(lambda x,y: x+y,l)

print(x)