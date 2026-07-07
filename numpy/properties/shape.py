# ------------------------------------------------------------------------------
# shape Attribute
# ------------------------------------------------------------------------------
# Used to find the dimensions (rows and columns) of a NumPy array.
#
# Syntax:
# array_name.shape
#
# Parameters:
# None (shape is an attribute, not a function)
#
# Returns:
# A tuple representing the dimensions of the array.
#
# For a 2D array:
# (number_of_rows, number_of_columns)
#
# Common Uses:
# • Check the size of an array
# • Verify dataset dimensions
# • Reshape arrays
# • Machine Learning & Data Analysis
# ------------------------------------------------------------------------------

import numpy as np

# Create a 2D array with 2 rows and 3 columns
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Display the shape of the array
print(arr_2d.shape)      # Output: (2, 3)


# import numpy as np
# arr_2d=np.array([[1,2,3],[4,5,6]])

# print(arr_2d.shape)
