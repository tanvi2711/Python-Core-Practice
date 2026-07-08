# -----------------------------------------
# Concatenate Arrays in NumPy
# -----------------------------------------

import numpy as np

arr1 = np.array([10, 20, 30])
arr2 = np.array([40, 50, 60])

# np.concatenate()
# Joins two or more arrays into a single array.

# Syntax:
# np.concatenate((array1, array2, ...), axis=0)

# Parameters:
# (array1, array2, ...)
#        -> Tuple containing the arrays to join.
# axis   -> Specifies the axis along which arrays are joined.
#
# axis = 0 -> Join row-wise (default for 1D arrays).
# axis = 1 -> Join column-wise (only for 2D arrays).

# Important:
# - All arrays must have the same data type (or be compatible).
# - For 2D arrays, dimensions must match except along
#   the concatenation axis.
# - np.concatenate() returns a NEW array.
# - Original arrays remain unchanged.

# Join two 1D arrays
# arr1 = [10 20 30]
# arr2 = [40 50 60]
#
# Result:
# [10 20 30 40 50 60]

new_arr = np.concatenate((arr1, arr2), axis=0)

print(new_arr)

