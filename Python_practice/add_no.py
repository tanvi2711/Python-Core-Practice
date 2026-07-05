a=int(input("1st number: "))
b=int(input("2nd number: "))

print(a+b)


l=[a,b]
print(sum(l))

print(a.__add__(b))

import operator

print(operator.add(a,b))

import math

print(math.fsum(l))