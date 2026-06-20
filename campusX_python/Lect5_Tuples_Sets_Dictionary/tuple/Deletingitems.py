# Deleting items

t=(1,3,2,4,1)

del t  # we can delete whole tuple but cant delete single item as it will consider as a change n tuples are immutable

# print(t)

t=(1,2,3,4,(2,4,3))
del t[-1]
print(t) # not work
