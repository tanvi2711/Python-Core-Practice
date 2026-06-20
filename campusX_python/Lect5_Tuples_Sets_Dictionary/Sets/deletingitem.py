# del
print("-------del-------")
s = {1,2,3,4,5}
# print(s)
# del s[0]
# print(s)



# discard
print("-------discard-------")
s.discard(5)
print(s)
s.discard(50)
print(s)


# remove
print("-------remove-------")
s.remove(4)
print(s)
# s.remove(50)
# print(s)



# pop
print("-------pop-------")
print(s.pop() )  #randomly delete any item



# clear
print("-------clear-------")
s.clear()
print(s)