# ------------------------------------------------------------------------------
# ndim Attribute
# ------------------------------------------------------------------------------
# Used to find the number of dimensions (axes) of a NumPy array.
#
# Syntax:
# array_name.ndim
#
# Parameters:
# None (ndim is an attribute, not a function)
#
# Returns:
# An integer representing the number of dimensions.
#
# Examples:
# 1D Array -> ndim = 1
# 2D Array -> ndim = 2
# 3D Array -> ndim = 3
# ------------------------------------------------------------------------------

import numpy as np

# Create a 2D array with 1 row and 3 columns
arr = np.array([[1, 2, 3]])

# Display the number of dimensions
print(arr.ndim)      # Output: 2

# ------------------------------
# Different Dimension Examples
# ------------------------------

# 1D Array
arr_1d = np.array([1, 2, 3])

# 2D Array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 3D Array
arr_3d = np.array([
    [
        [1, 2],
        [5, 6],
        [5, 3],
        [4, 6],
        [7, 8]
    ]
])

print("1D Array:", arr_1d.ndim)   # Output: 1
print("2D Array:", arr_2d.ndim)   # Output: 2
print("3D Array:", arr_3d.ndim)   # Output: 3