# Problem-9` Write a python function that accepts a list of 2D co-ordinates and a query point, and then finds the the co-ordinate which is closest in terms of distance from the query point.

# List of Coordinates
# [(1,1),(2,2),(3,3),(4,4)]
# Query Point
# (0,0)

# Output
# Nearest to (0,0) is (1,1)

import math

def distance(l,q):
    dis=0
    for i in l:
        x=i[0]
        x0=0
        y=i[0]
        y0=0
        dis=((x-x0)**2+(y-y0)**2)**0.5
        print(dis)


distance([(1,1),(2,2),(3,3),(4,4)],(0,0))





