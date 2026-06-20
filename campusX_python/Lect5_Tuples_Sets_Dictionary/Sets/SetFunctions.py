# Set Functions

# len/sum/min/max/sorted
s = {3,1,4,5,2,7}

print("--------------len/sum/min/max/sorted--------------")
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s,reverse=True))


# union/update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print("------------union------------")
# s1 | s2
print(s1.union(s1))

print("------------update------------")
s1.update(s2)
print(s1)
print(s2)


# intersection/intersection_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print("------------intersection------------")
print(s1.intersection(s2))

print("------------intersection_update------------")
s1.intersection_update(s2)
print(s1)
print(s2)


# difference/difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print("------------difference------------")
print(s1.difference(s2))

print("------------difference_update------------")
s1.difference_update(s2)
print(s1)
print(s2)


# symmetric_difference/symmetric_difference_update
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print("------------symmetric_difference------------")
print(s1.symmetric_difference(s2))

print("------------symmetric_difference_update------------")
s1.symmetric_difference_update(s2)
print(s1)
print(s2)


# isdisjoint/issubset/issuperset
s1 = {1,2,3,4}
s2 = {7,8,5,6}

print("------------isdisjoint------------")
print(s1.isdisjoint(s2))  # disjoin sets means not a single item is simalar in sets


s1 = {1,2,3,4,5}
s2 = {3,4,5}

print("------------issubset------------")
print(s2.issubset(s1)) #subset means 2nd set is in 1st set
print(s1.issubset(s2))

s1 = {1,2,3,4,5}
s2 = {3,4,5}

print("------------issuperset------------")
print(s1.issuperset(s2))


# copy
print("------------copy------------")
s1 = {1,2,3}
s2 = s1.copy()
print(s1)
print(s2)