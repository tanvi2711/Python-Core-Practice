"""
-----------------------------------------
Splitting Arrays in NumPy
-----------------------------------------

Functions:
np.split()  -> Split an array into equal parts.
np.vsplit() -> Split a 2D array vertically (row-wise).
np.hsplit() -> Split a 2D array horizontally (column-wise).
"""

import numpy as np

# -----------------------------------------
# split() - 1D Array
# -----------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Syntax:
# np.split(array, number_of_parts)

# Important:
# - Splits the array into equal-sized sub-arrays.
# - Total elements must be divisible by the number of parts.
# - Returns a list of NumPy arrays.
# - If equal splitting is not possible, a ValueError is raised.

# Split into 2 equal parts
# Result:
# [array([1,2,3,4]), array([5,6,7,8])]

print(np.split(arr, 2), '\n')

# Split into 4 equal parts
# Result:
# [array([1,2]), array([3,4]), array([5,6]), array([7,8])]

print(np.split(arr, 4), '\n')

# Cannot split 8 elements into 3 equal parts.
# Raises ValueError.
# print(np.split(arr, 3))

# -----------------------------------------
# vsplit() and hsplit() - 2D Array
# -----------------------------------------

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

# -----------------------------------------
# Vertical Split (vsplit)
# -----------------------------------------

# Syntax:
# np.vsplit(array, number_of_parts)

# Splits the array row-wise.
# Each split contains complete rows.

# Original:
# [[1 2 3 4]
#  [5 6 7 8]]
#
# Result:
# [array([[1,2,3,4]]),
#  array([[5,6,7,8]])]

print(np.vsplit(arr, 2), '\n')

# -----------------------------------------
# Horizontal Split (hsplit)
# -----------------------------------------

# Syntax:
# np.hsplit(array, number_of_parts)

# Splits the array column-wise.
# Each split contains complete columns.

# Original:
# [[1 2 3 4]
#  [5 6 7 8]]
#
# Result:
# [array([[1,2],
#         [5,6]]),
#
#  array([[3,4],
#         [7,8]])]

print(np.hsplit(arr, 2))