import math

import numpy as np

num=int(input("Enter any no: "))

print(math.factorial(num))

fact=1

for i in range(1,num+1):
    fact*=i

print(fact)


import numpy as np

if num >= 0:
    print(np.prod(range(1, num+1)))  
else:
    print("Factorial is not defined for negative numbers")




def factorial(num):
    if num<0:
        return "Factorial is not defined for negative numbers"
    return True if num<=1 else num*factorial(num-1)
    
print(factorial(num))
