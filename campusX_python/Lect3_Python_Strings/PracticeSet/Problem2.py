# Problem 2: Print the following pattern.

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *


num=int(input("Enter no of rows: " ))



for i in range(1,(num//2+1)+1):
    for j in range(1,i+1):
        print("* ",end='')
    print()

for k in range(num//2,0,-1):
    for l in range(k,0,-1):
        print("* ",end='')
    print()
