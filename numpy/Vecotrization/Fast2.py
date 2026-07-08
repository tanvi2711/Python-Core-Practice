# ==========================================
# NumPy Vectorization + Broadcasting Example
# ==========================================

import numpy as np

arr = np.array([100, 200, 300])

# Here both Vectorization and Broadcasting are used.

# Broadcasting:
# '3' is a scalar (single value).
# NumPy automatically broadcasts it to every
# element of the array.
#
# It behaves as if:
# [3 3 3]
#
# (This array is NOT actually created.)

# Vectorization:
# NumPy multiplies the entire array at once
# without using a Python for loop.

# Backend Working:
#
# [100 200 300]
# *
# [  3   3   3]
# =
# [300 600 900]

multiply = arr * 3

print(multiply)

# -----------------------------------------
# Output
# -----------------------------------------

# [300 600 900]