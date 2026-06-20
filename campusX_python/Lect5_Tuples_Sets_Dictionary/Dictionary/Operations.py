# Dictionary Operations


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

# Membership
print('name' in s)
print('tanvi' in s)  # its not key thats why false 


# Iteration
for i in s:
    print(f"{i} : {s[i]}")
