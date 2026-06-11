# Accessing Items from a List

print("----------Accessing Items from a List----------")


# indexing

print("indexing")
l=[1,2,3,4,5]
# positive
print(l[0])
print(l[-1])

l=[1,2,3,[4,5]]
print(l[-1])
print(l[-1][-1])
print(l[-1][-2])
print(l[3][0])

l=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(l[1][0][0])


#slicing
l=[1,2,3,4,5]

print("slicing")
print(l[1:5])
print(l[1:])
print(l[:-1])
print(l[-2:])

print(l[0::2])  #2 is step here
print(l[ -5:-2:2])

print("reverse")
print(l[::-1])
