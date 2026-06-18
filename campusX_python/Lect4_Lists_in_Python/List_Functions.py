# List Functions
print("-------------List Functions--------------")

# len/min/max/sorted
l=[1,2,3,32,4,5,6]

print(len(l))
print(min(l))
print(max(l))
print(sorted(l))
print(sorted(l,reverse=True))


# count 
l=[1,2,1,4,2,1,3,4,2]
print(l.count(2))

# index
print(l.index(4))

# reverse
l=[1,4,3,32,9,4,8,6]
l.reverse() # permanently reverses the list
print(l)

# sort (vs sorted)
l=[1,4,3,32,9,4,8,6]
print(sorted(l))  #temprory operation no change in original
print(l)
l.sort() #permanent operation
print(l)

# copy -> shallow                                  
l=[1,4,4,8,6]
print(l)
print(id(l))
l1=l.copy()
print(l1)
print(id(l1))