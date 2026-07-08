# ==========================================
# Broadcasting with a 2D Array and a 1D Array
# ==========================================

import numpy as np

matrix = np.array([[100, 200, 300],
                   [400, 500, 600]])

vector = np.array([10, 20, 30])

print("Matrix:")
print(matrix)

print("\nVector:")
print(vector)

# -----------------------------------------
# Broadcasting
# -----------------------------------------

# Shapes:
# matrix -> (2, 3)
# vector -> (3,)
#
# Since the last dimension of both arrays is 3,
# NumPy broadcasts the 1D vector across every row
# of the 2D matrix.

# Backend Working:
#
# Matrix
#
# [[100 200 300]
#  [400 500 600]]
#
# Vector
#
# [10 20 30]
#
# NumPy behaves as if the vector becomes:
#
# [[10 20 30]
#  [10 20 30]]
#
# NOTE:
# This expanded array is NOT actually created.
# NumPy only treats it as if it exists.

# Element-wise Addition:
#
# [[100 200 300]
#  [400 500 600]]
#
# +
#
# [[10 20 30]
#  [10 20 30]]
#
# =
#
# [[110 220 330]
#  [410 520 630]]

result = matrix + vector

print("\nResult:")
print(result)

# -----------------------------------------
# Why Broadcasting Works?
# -----------------------------------------

# matrix shape = (2, 3)
# vector shape = (3,)
#
# NumPy compares dimensions from right to left.
#
# Last Dimension:
# 3 == 3 ✔ Compatible
#
# Missing first dimension of the vector is treated as 1.
#
# matrix : (2, 3)
# vector : (1, 3)
#
# Since one dimension is 1,
# NumPy stretches it to:
#
# (2, 3)
#
# Therefore, broadcasting is possible.

# -----------------------------------------
# Final Output
# -----------------------------------------

# [[110 220 330]
#  [410 520 630]]