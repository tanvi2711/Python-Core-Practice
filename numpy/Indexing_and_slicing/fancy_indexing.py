import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 7, 8, 9])

print("--------------Fancy Indexing----------------")

# Fancy Indexing:
# Instead of a single index, we pass a list (or array) of indices.
# NumPy picks the elements at those positions and returns them
# in the same order as the indices provided.

# Important:
# Fancy indexing creates a NEW array (copy), not a view.
# Any changes made to the returned array will NOT affect the original array.

print(arr[[0, 5, 2, 6, 3]])

# Here NumPy performs the following internally:
# Index :   [0, 5, 2, 6, 3]
# Value :   [1, 6, 3, 7, 4]
# A new array is created with these values.

print(arr[[0, 2, 4, 6, 8]])

# Selecting alternate elements using their indices.
# Since a copy is returned, modifying the result will not
# change the original array.