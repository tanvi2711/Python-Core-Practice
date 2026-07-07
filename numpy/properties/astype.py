# ------------------------------------------------------------------------------
# astype() Method
# ------------------------------------------------------------------------------
# Used to convert the data type (dtype) of a NumPy array.
#
# Syntax:
# array_name.astype(new_dtype)
#
# Parameters:
# new_dtype -> The desired data type (Required)
#              Examples: int, float, str, bool
#
# Returns:
# A new NumPy array with the specified data type.
#
# Note:
# • astype() does NOT modify the original array.
# • It returns a new array with the converted data type.
#
# Common Uses:
# • Convert float to int
# • Convert int to float
# • Prepare data for Machine Learning
# • Reduce memory usage by changing data types
# ------------------------------------------------------------------------------

import numpy as np

# Create an array of float values
arr = np.array([1.3, 3.7, 8.2])

# Convert the array from float to integer
# (Decimal part is removed, not rounded)
int_arr = arr.astype(int)

print(int_arr)         # Output: [1 3 8]
print(int_arr.dtype)   # Output: int64 (or int32 depending on the system)


# import numpy as np
# arr_2d=np.array([1.3,3.7,8.2])

# int_arr=arr_2d.astype(int)

# print(int_arr)
# print(int_arr.dtype)