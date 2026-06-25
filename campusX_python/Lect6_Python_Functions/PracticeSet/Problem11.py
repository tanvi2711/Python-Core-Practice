# Problem 11:` Write a Python program to add three given lists using Python map and lambda.


l1,l2,l3=[1,2,3],[3,5,2],[2,8,4]

add=list(map(lambda x,y,z: x+y+z,l1,l2,l3))

print(add)