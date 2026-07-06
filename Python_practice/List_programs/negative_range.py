# given start and end point start, end = -5, 0 we need to print all numbers so that output should be -5 -4 -3 -2 -1.

a=[]
for i in range(-5,0):
    if i<0:
        a.append(i)

print(a)