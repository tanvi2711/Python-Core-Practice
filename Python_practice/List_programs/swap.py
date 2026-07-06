a = [10, 20, 30, 40, 50]

l=len(a)//2

for i,j in zip(range(l),range(len(a)-1,l,-1)):
    a[i],a[j]=a[j],a[i]
    

print(a)