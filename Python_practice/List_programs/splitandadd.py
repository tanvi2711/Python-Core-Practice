l=[]
n=int(input("Enter range of list: "))
for i in range(n):
    i=int(input("Enter no: "))
    l.append(i)

d=int(input("Enter Number: "))

a=[]

a=l[d:]+l[:d]

print(a)