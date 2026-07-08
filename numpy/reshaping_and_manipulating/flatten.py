"""
.ravel()-->View
.flatten()-->copy

"""

import numpy as np

print("--------------Flattening Arrays----------------")

arr = np.array([[10,  20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr, end="\n\n")

# -----------------------------------------
# ravel()
# -----------------------------------------

# Converts a multi-dimensional array into a 1D array.

# Important:
# - Returns a VIEW whenever possible.
# - Changes made to the returned array may also
#   affect the original array.

print(arr.ravel(), end="\n\n")

# -----------------------------------------
# flatten()
# -----------------------------------------

# Converts a multi-dimensional array into a 1D array.

# Important:
# - Always returns a COPY of the original array.
# - Changes made to the flattened array will NOT
#   affect the original array.

print(arr.flatten())

# -----------------------------------------
# Difference between ravel() and flatten()
# -----------------------------------------

# ravel()
# ✔ Faster
# ✔ Returns a View (whenever possible)
# ✔ Shares memory with the original array

# flatten()
# ✔ Slightly slower
# ✔ Always returns a Copy
# ✔ Does NOT share memory with the original array