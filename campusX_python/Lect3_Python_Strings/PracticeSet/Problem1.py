# Problem 1 - Print the following pattern. Write a program to use for loop to print the following reverse number pattern.


# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

num=int(input("Enter no of rows: " ))

for i in range(num+1,1,-1):
    print("i",i)
    for j in range(i-1,0,-1):
        print(j,end=' ' )
    print()

