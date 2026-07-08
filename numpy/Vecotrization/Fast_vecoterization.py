# ==========================================
# NumPy Vectorization
# ==========================================

import numpy as np

arr1 = np.array([100, 200, 300])
arr2 = np.array([400, 500, 600])

# Vectorization:
# Vectorization means performing an operation on
# the entire array at once without using Python loops.

# Both arrays have the same shape.
#
# arr1 -> (3,)
# arr2 -> (3,)
#
# NumPy performs element-wise addition internally.

# Backend Working:
#
# [100 200 300]
# +
# [400 500 600]
# =
# [500 700 900]

# Internally, NumPy performs:
#
# 100 + 400 = 500
# 200 + 500 = 700
# 300 + 600 = 900
#
# This is done in optimized C code,
# not using a Python for loop.

result = arr1 + arr2

print(result)

# -----------------------------------------
# Output
# -----------------------------------------

# [500 700 900]