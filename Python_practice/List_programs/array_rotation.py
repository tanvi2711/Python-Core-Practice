l=[]
n=int(input("Enter range of list: "))
for i in range(n):
    i=int(input("Enter no: "))
    l.append(i)

d=int(input("Enter Number: "))

a=[]

for i in range(len(l)):
    if i==d:
        a.append(l[i])
        d+=1
    
a.extend(l[0:len(a)-1])
print(a)