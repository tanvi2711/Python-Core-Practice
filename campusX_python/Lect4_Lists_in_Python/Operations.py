# Operations on Lists
print("---------Operations on Lists----------")

l=[1,2,3,4]
l1=[3,4,5,6]

# Arithmetic (+,*)
print(l+l1)
print(l*3) #l*l*l

# Membership
print(5 in l)
print(5 not in l)

l2=[3,4,5,6,[7,8]]
print(7 in l2)                            

# Loop
s=[]

n=int(input("How many no u want in list:"))

for i in range(1,n+1):
    j=int(input(f"Enter {i} element: "))
    s.append(j)

print(s)