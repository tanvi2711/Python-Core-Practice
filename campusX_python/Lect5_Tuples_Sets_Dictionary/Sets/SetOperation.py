# Set Operation

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

# Union(|)
print("-------Union(|)--------")
print(s1 | s2)

# Intersection(&)
print("-------Intersection(&)--------")
print(s1 & s2)


# Difference(-)
print("-------Difference(-)--------")
print(s1 - s2)  # s1 ke  wo item jo s2 me present nahi hai
print(s2 - s1)  # s2 ke  wo item jo s1 me present nahi hai


# Symmetric Difference(^)
print("-------Symmetric Difference(^)--------")
print(s1 ^ s2)



# Membership Test
print("-------Membership Test--------")
print(1 not in s1)


# Iteration
print("-------loop--------")
for i in s1:
  print(i)