# ## Adding Items to a List
l=[1,2,3,4,5,6]
print("----------Adding Items to a List----------")

# append
print("append")   #append used to add one item in list
l.append(0) 
print(l)
l.append([9,0]) 
print(l)

# extend
print("extend")  #extend used to add multiple item in list
l=[1,2,3,4,5]
l.extend("hello")
l.extend(["hello"])
l.extend([9,0 ,[00,78],'tanvi',True])
print(l)


# insert
print("insert") # if i have to insert any elemnt at any position 
l=[1,2,3,4,5]
l.insert(1,60)
print(l)
