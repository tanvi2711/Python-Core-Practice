# Given a list of elements and a number n, the task is to split the list into smaller sublists (chunks), where each sublist contains at most n elements. This helps in processing large data in smaller parts or batches.

# For Example:

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# n = 3
# Result: [[1, 2, 3], [4, 5, 6], [7, 8]]

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = 3 
res = [a[i:i + n] for i in range(0, len(a), n)]
print(res)