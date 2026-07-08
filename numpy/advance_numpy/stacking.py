"""
-----------------------------------------
Stacking Arrays in NumPy
-----------------------------------------

Vertical Stacking
Horizontal Stacking

Functions:
np.vstack() -> Stack arrays row-wise (vertically)
np.hstack() -> Stack arrays column-wise (horizontally)
"""

import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# -----------------------------------------
# Vertical Stack (vstack)
# -----------------------------------------

# Syntax:
# np.vstack((array1, array2, ...))

# Stacks arrays one below another.
# Each input array becomes a separate row.

# Important:
# - All arrays must have the same number of columns.
# - Returns a NEW 2D array.
# - Original arrays remain unchanged.

# arr1 = [1 2 3 4]
# arr2 = [5 6 7 8]
#
# Result:
# [[1 2 3 4]
#  [5 6 7 8]]

print(np.vstack((arr1, arr2)), "\n")

# -----------------------------------------
# Horizontal Stack (hstack)
# -----------------------------------------

# Syntax:
# np.hstack((array1, array2, ...))

# Stacks arrays side by side.
# For 1D arrays, it joins them into a single array.

# Important:
# - Arrays must have compatible dimensions.
# - Returns a NEW array.
# - Original arrays remain unchanged.

# arr1 = [1 2 3 4]
# arr2 = [5 6 7 8]
#
# Result:
# [1 2 3 4 5 6 7 8]

print(np.hstack((arr1, arr2)))