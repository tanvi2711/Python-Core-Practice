# ------------------------------------------------------------------------------
# size Attribute
# ------------------------------------------------------------------------------
# Used to find the total number of elements in a NumPy array.
#
# Syntax:
# array_name.size
#
# Parameters:
# None (size is an attribute, not a function)
#
# Returns:
# An integer representing the total number of elements.
#
# Formula:
# Total Elements = Rows × Columns × Depth (for multi-dimensional arrays)
#
# Common Uses:
# • Count total elements in an array
# • Check dataset size
# • Validate array dimensions before processing
# ------------------------------------------------------------------------------

import numpy as np

# Create a 2D array with 2 rows and 3 columns
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

# Display the total number of elements
print(arr_2d.size)      # Output: 6

# import numpy as np
# arr_2d=np.array([[1,2,3],[4,5,6]])

# print(arr_2d.size)


