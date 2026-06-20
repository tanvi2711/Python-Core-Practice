print("--------list--------")
a = [1,2,3]
b = a

a.append(4)
print(a)
print(b)

print("---------tuple-------")
a = (1,2,3)
b = a

a = a + (4,)
print(a)
print(b)