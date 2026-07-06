l=[]
n=int(input("Enter range of list: "))
for i in range(n):
    i=int(input("Enter no: "))
    l.append(i)


lar=0

for i in l:
    if lar>i:
        break
    else:
        lar=i

print("Largest: ",lar)