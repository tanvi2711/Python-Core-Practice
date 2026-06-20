# empty
s={} #dict not set
s = set()
print(s)
print(type(s))


# 1D and 2D
s = {1,2,3}
print(s)

#s2 = {1,2,3,{4,5}}  #not allow 
#print(s2)



# homo and hetro
s= {1,'hello',4.5,(1,2,3),True}
print(s)   # sets are unordered it based on hashing we cant change it its inbulit str 




# using type conversion
s = set([1,2,3])
print(s)


# duplicates not allowed
s = {1,1,2,2,3,3}
print(s)


# set can't have mutable items
# s = {1,2,[3,4]}
# print(s)


s1={1,2,3}
s2={3,2,1}
print(s2==s1)  # order doesnt matter only contains are checked here

