# Q1`: Key with maximum unique values

# Given a dictionary with values list, extract key whose value has most unique values.

# **Example 1:**

# Input:
# test_dict = {"CampusX" : [5, 7, 9, 4, 0], "is" : [6, 7, 4, 3, 3], "Best" : [9, 9, 6, 5, 5]}

# Output:
# CampusX

test_dict = {"CampusX" : [5, 7, 7, 7, 7], "is" : [6, 7, 7, 7], "Best" : [9, 9, 6, 5, 5]}

l=[]

for i in test_dict:
    test_dict[i]=set(test_dict[i])
    l.append(len(test_dict[i]))

for i in test_dict:
    if len(test_dict[i])==max(l):
        print(i)
