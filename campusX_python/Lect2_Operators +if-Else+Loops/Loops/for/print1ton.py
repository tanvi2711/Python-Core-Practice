num=int(input("Enter any no: "))

print("Print 1 to n")
for i in range(1,num+1):
    print(i)

print("Print 1 to n with the gap of 2")
for i in range(1,num+1,2):
    print(i)

print("Print 1 to n in reverse order")
for i in range(num,0,-1):
    print(i)


print("Print list")
for i in [1,2,3,4,5,9]:
    print(i)