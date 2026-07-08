# -----------------------------------------
# Append Elements in a NumPy Array
# -----------------------------------------

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# np.append()
# Adds element(s) at the END of an array.

# Syntax:
# np.append(array, values, axis=None)

# Parameters:
# array  -> Original array.
# values -> Value or values to append.
# axis   -> None (default) for 1D arrays.
#           0 -> Append rows (2D array)
#           1 -> Append columns (2D array)

# Important:
# - np.append() always returns a NEW array.
# - The original array remains unchanged.
# - For 1D arrays, axis=None is used by default.

# Append multiple elements at the end
# Original:
# [10 20 30 40 50 60]
#
# Result:
# [10 20 30 40 50 60 70 80 90 100]

new_arr = np.append(arr, [70, 80, 90, 100])

print(new_arr)
