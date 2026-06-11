print("------------traverse a list-------------")
# 2 ways to traverse a list


print("---------itemwise------------")
# itemwise
l=[1,3,4,2,4]
for i in l:
    print(i)


print("-------indexwise-----------")
# indexwise
for i in range(0,len(l)):
    print(f"{i} is index of {l[i]}")