# Given a list containing multiple sublists, the task is to remove all empty sublists from it. Removing empty lists means keeping only the sublists that have at least one element.

# For example:

# a = [[1, 2], [], [3, 4], [], [5]]
# Resulting list = [[1, 2], [3, 4], [5]]

a = [[1, 2], [], [3, 4], [], [5]]

for i in a:
    if i == []:
        a.remove(i)

print(a)