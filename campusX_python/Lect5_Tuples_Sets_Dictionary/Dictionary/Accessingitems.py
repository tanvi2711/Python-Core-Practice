d={'name':'tanvi','age':21}

# print(d[1])  not allowed


# using keys
print(d['name'])

# get
print(d.get('age'))



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
print(s['subjects'])
print(s['subjects']['maths'])