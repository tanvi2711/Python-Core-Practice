# Q2`: Replace words from Dictionary. Given String, replace it’s words from lookup dictionary.

# Example 1:

# Input:
# test_str = 'CampusX best for DS students.'
# repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

# Output:
# CampusX is the best channel for Data-Science students.

test_str = 'CampusX best for DS students.'
repl_dict = {"best" : "is the best channel", "DS" : "Data-Science"}

s=test_str.split()

b=''

for i in s:
    if i in repl_dict:
        i=repl_dict[i]
        d=" "
        b=b+d+i+d
    else:
        b=b+i
print(b)


# b=[]

# for i in s:
#     if i in repl_dict:
#         i=repl_dict[i]
#         b.append(i)
#     else:
#         b.append(i)
# print(' '.join(b))