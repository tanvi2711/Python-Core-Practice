# Problem-1: Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Input:
# [1,2,3,3,3,3,4,5]

# Output:
# [1, 2, 3, 4, 5]


def unique_list(l):
    l=set(l)
    return list(l)


print(unique_list([1,2,3,3,3,3,4,5]))

