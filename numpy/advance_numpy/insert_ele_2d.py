# -----------------------------------------
# Insert Elements in a 2D Array
# -----------------------------------------

import numpy as np

arr2d = np.array([[10, 20, 30],
                  [40, 50, 60]])

# np.insert() returns a NEW array.
# The original array remains unchanged.

# axis = 0  -> Insert row(s)
# axis = 1  -> Insert column(s)

# Insert a column containing the value 25 at column index 2.
# The value 25 is inserted for every row.

# Original:
# [[10 20 30]
#  [40 50 60]]
#
# Result:
# [[10 20 25 30]
#  [40 50 25 60]]

new_arr2d = np.insert(arr2d, 2, 25, axis=1)

print(new_arr2d)

# Original array is unchanged
print(arr2d)