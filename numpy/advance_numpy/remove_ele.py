# -----------------------------------------
# Delete Elements from a NumPy Array
# -----------------------------------------

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Display the original array
print(arr)

# np.delete()
# Removes element(s) from an array and returns
# a NEW array.

# Syntax:
# np.delete(array, index, axis=None)

# Parameters:
# array -> Original array.
# index -> Index (or indices) of the element(s) to delete.
# axis  -> None (default): Treat the array as 1D.
#          0 : Delete row(s) from a 2D array.
#          1 : Delete column(s) from a 2D array.

# Important:
# - np.delete() does NOT modify the original array.
# - It creates and returns a NEW array.
# - The element at index 1 (value 20) is removed.

# Original:
# [10 20 30 40 50 60]
#
# Delete index 1
#
# Result:
# [10 30 40 50 60]

new_arr = np.delete(arr, 1, axis=None)

print(new_arr)

# If we print the original array again,
# it is still unchanged because np.delete()
# created a new array instead of modifying it.

print(arr)
