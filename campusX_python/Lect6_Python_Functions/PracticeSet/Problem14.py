# Problem-14`: Use reduce to convert a 2D list to 1D

import functools

l=[
    [1,2,3,4],
    [4,6,1,8]
]

x=list(functools.reduce(lambda x,y:x+y,l))

print(list(x))