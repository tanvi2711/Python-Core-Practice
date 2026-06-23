# Q3`: Check is tuples are same or not?
# Two tuples would be same if both tuples have same element at same index
# t1 = (1,2,3,0)
# t2 = (0,1,2,3)

# t1 and t2 are not same


t1=[]
t2=[]

n1=int(input("Enter how many no do u want in tuple1:"))
n2=int(input("Enter how many no do u want in tuple2:"))

if n1!=n2:
    exit("Tuple length is no same")


print("Enter items of t1")
for i in range(n1):
    i=int(input("Enter no: "))
    t1.append(i)

print("Enter items of t2")
for i in range(n2):
    i=int(input("Enter no: "))
    t2.append(i)

t1=tuple(t1)
t2=tuple(t2)

print(t1)
print(t2)

flag=0


for i,j in zip(t1,t2):
    if i==j:
        flag=True
    else:
        flage=False
        break

if flag==True:
    print("t1 and t2 are same") 
else:
    print("t1 and t2 are not same")    
