# Q4:- Write a program to find the euclidean distance between two coordinates.Take both the coordinates from the user as input.

# d = √[ (x2 – x1  )^2 + (y2 – y1 )^2]

x1=int(input("Enter any no : "))
x2=int(input("Enter any no : "))
y1=int(input("Enter any no : "))
y2=int(input("Enter any no : "))

euclidean_distance=( (x2-x1)**2 + (y2-y1)**2)** 0.5   # square root == **0.5
print("Euclidean distance between given two coordinates is : ",euclidean_distance)
