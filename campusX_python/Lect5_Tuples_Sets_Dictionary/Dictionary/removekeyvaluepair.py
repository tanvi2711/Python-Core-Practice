d = {'name': 'nitish', 'age': 32, 3: 3, 'gender': 'male', 'weight': 72}


# pop
print("---------pop-----------")
d.pop(3)
# d.pop('gender')
print(d)



# popitem
print("---------popitem-----------")
# d.popitem()
d.popitem()
print(d)



# del
print("---------del-----------")
del d['name']
print(d)


# clear
print("---------clear-----------")
d.clear()
print(d)

