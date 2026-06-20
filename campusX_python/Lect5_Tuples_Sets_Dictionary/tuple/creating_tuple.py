# empty tuple

t=()
print(t)

# create a tuple with a single item
t=('hello')
print(t)
print(type(t))  #str


t=('hello',)
print(t)
print(type(t))  #tuple


# homo
t=(1,3,2,4,1)
print(t)


# hetro
t=(1,4,'str',(5+9j),True,[1,2,3],3.4)
print(t)

# 2d tuple
t=(1,2,3,4,(2,4,3))
print(t)

# using type conversion
print(tuple("hello"))