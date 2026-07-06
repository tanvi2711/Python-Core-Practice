# Given a list that contains both empty and non-empty tuples, the task is to remove all empty tuples from the list. For Example:

# Input: [(1, 2), (), (3, 4), (), (5,)]
# Output: [(1, 2), (3, 4), (5,)]


a = [(1, 2), (), (3, 4), (), (5,)]

for i in a:
    if i == ():
        a.remove(i)

print(a)