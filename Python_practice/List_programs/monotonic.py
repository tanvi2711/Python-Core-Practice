l=[]
n=int(input("Enter range of list: "))
for i in range(n):
    i=int(input("Enter no: "))
    l.append(i)


if sorted(l)==l or sorted(l,reverse=True)==l:
    print("True")
else:
    print("False")