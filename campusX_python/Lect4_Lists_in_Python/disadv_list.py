# Disadvantages of Python Lists
# Slow
# Risky usage
# eats up more memory

print("-----------Risky usage------------")
a=[1,2,3]
# b=a
b=a.copy()  # if we did this it will point diff memory locations 
print(a)
print(b)

a.append(4)
print(a)
print(b)

# Becoz list are mutabble when we did a=b it will point same memory location

