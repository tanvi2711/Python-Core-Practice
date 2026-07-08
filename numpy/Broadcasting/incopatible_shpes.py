# ==========================================
# Broadcasting with Incompatible Shapes
# ==========================================

import numpy as np

arr = np.array([[100, 200, 300],
                [400, 500, 600]])

vector = np.array([10, 20])

print("Matrix Shape :", arr.shape)
print("Vector Shape :", vector.shape)

# -----------------------------------------
# Broadcasting Check
# -----------------------------------------

# Matrix Shape : (2, 3)
# Vector Shape : (2,)

# NumPy compares shapes from RIGHT to LEFT.

# Matrix : (2, 3)
# Vector :    (2,)
#
# Compare last dimensions:
#
# 3  vs  2
#
# They are:
# ✘ Not equal
# ✘ Neither dimension is 1
#
# Therefore, broadcasting is NOT possible.

# NumPy cannot virtually expand the vector
# because the last dimensions are incompatible.

# This statement raises a ValueError.

result = arr + vector

print(result)

# -----------------------------------------
# Expected Error
# -----------------------------------------

# ValueError:
# operands could not be broadcast together
# with shapes (2,3) (2,)

