s = {
    'name':'nitish',
     'college':'bit',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}

print("Length: ",len(s))
print("Sorted: ",sorted(s))
print("Sorted: ",sorted(s,reverse=True))
print("Max: ",max(s))
print("Min: ",min(s))


# items/keys/values
print("-----------items/keys/values------------")
print(s.items())
print(s.keys())
print(s.values())

# update
print("----------update-----------")
d1 = {1:2,3:4,4:5}
d2 = {4:7,6:8}

d1.update(d2)
print(d1)

