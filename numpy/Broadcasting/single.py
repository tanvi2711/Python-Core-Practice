# ==========================================
# Broadcasting with a Scalar
# ==========================================

import numpy as np

arr = np.array([100, 200, 300, 400])

print("Original Array:")
print(arr)

# Scalar value
scalar = 2

# -----------------------------------------
# Broadcasting
# -----------------------------------------

# Here, '2' is a scalar (single value).
# NumPy automatically broadcasts the scalar
# to every element of the array.

# Shape:
# arr    -> (4,)
# scalar -> ()

# Backend Working:
#
# Original Array
# [100 200 300 400]
#
# Scalar
# 2
#
# NumPy behaves as if:
#
# [2 2 2 2]
#
# NOTE:
# This array is NOT actually created in memory.
# NumPy only behaves as if it exists.

# Element-wise Multiplication:
#
# [100 200 300 400]
#
# *
#
# [2 2 2 2]
#
# =
#
# [200 400 600 800]

result = arr * scalar

print("\nResult:")
print(result)

# -----------------------------------------
# Why Broadcasting Works?
# -----------------------------------------

# arr shape    = (4,)
# scalar shape = ()
#
# A scalar can be broadcast to any array shape.
# NumPy automatically applies the scalar
# to every element of the array.

# -----------------------------------------
# Output
# -----------------------------------------

# [200 400 600 800]