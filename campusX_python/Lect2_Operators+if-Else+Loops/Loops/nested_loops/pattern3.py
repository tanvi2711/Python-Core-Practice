# 1
# 121
# 12321
# 1234321

row=int(input("Enter rows: "))

for i in range(1,row+1):
    for j in range(1,i):
        print(j,end='')
    print(i,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    print()