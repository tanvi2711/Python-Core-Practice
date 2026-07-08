# ==========================================
# Replace Missing Values (NaN)
# ==========================================

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# np.nan_to_num()
# Replaces NaN values with a specified number.

# Syntax:
# np.nan_to_num(array, nan=value)

# Parameters:
# array -> Input array containing NaN values.
# nan   -> Value used to replace NaN.
#         Default value is 0.

# Important:
# - Returns a NEW array.
# - The original array remains unchanged.
# - Useful for cleaning data before analysis.

# Replace all NaN values with 10
print(np.nan_to_num(arr, nan=10))

# Output:
# [ 1.  2. 10.  4. 10.  6.]

print()

# Original array remains unchanged
print(arr)

# Output:
# [ 1.  2. nan  4. nan  6.]

# -----------------------------------------
# Default Behavior
# -----------------------------------------

# If 'nan' is not specified,
# NaN values are replaced with 0.

# Example:
# print(np.nan_to_num(arr))

# Output:
# [1. 2. 0. 4. 0. 6.]