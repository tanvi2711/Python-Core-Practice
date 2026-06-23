# Q2:Multiply Adjacent elements (both side) and take sum of right and lest side multiplication result. 

# For eg.
# The original tuple : (1, 5, 7, 8, 10)
# Resultant tuple after multiplication : 

# (1*5, 1*5 + 5*7, 7*5 + 7*8, 8*7 + 8*10, 10*8) -> (5, 40, 91, 136, 80)

# output-(5, 40, 91, 136, 80)


t=(1, 5, 7, 8, 10)

mul=1

for i in range(len(t)):
    if i>len(t):
        break
    if i == -1:
        i=i
    else:
        mul=t[i-1]*t[i]+t[i]*t[i+1]
    print(t[i-1],t[i],t[i+1])
    
    print(mul)
