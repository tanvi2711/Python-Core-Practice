# -----------------------------------------
# Delete Rows from a 2D NumPy Array
# -----------------------------------------

import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

# Display the original array
print(arr,"\n")

# np.delete()
# Removes row(s) or column(s) from an array.

# Syntax:
# np.delete(array, index, axis)

# axis = 0 -> Delete row(s)
# axis = 1 -> Delete column(s)

# Important:
# - np.delete() returns a NEW array.
# - The original array remains unchanged.

# Delete the row at index 0 (first row)
#
# Original:
# [[10 20 30]
#  [40 50 60]]
#
# Result:
# [[40 50 60]]

new_arr = np.delete(arr, 0, axis=0)

print(new_arr)
