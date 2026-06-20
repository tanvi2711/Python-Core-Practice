# Accessing Items


# Indexing
print("---------Indexing---------")
t=(1,2,3,4,5,6)

print(t[4])
print(t[0])
print(t[-1])

# Slicing
print("-------Slicing---------")
print(t[0:])
print(t[0:4])
print(t[-3:-1])
print(t[::-1])


print("-------2d tuple---------")
t=(1,2,3,4,(2,4,3))

print(t[4][1])
print(t[4][2])
print(t[-1][2])