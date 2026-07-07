# ------------------------------------------------------------------------------
# dtype Attribute
# ------------------------------------------------------------------------------
# Used to find the data type of elements stored in a NumPy array.
#
# Syntax:
# array_name.dtype
#
# Parameters:
# None (dtype is an attribute, not a function)
#
# Returns:
# The data type (dtype) of the array elements.
#
# Common Data Types:
# int32 / int64   -> Integer
# float32 / float64 -> Floating Point Number
# bool            -> Boolean
# complex64 / complex128 -> Complex Numbers
# str / object    -> String or Mixed Objects
#
# Common Uses:
# • Check the data type of an array
# • Optimize memory usage
# • Convert data to another type using astype()
# • Required in Data Science & Machine Learning
# ------------------------------------------------------------------------------

import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3]])

# Display the data type of array elements
print(arr.dtype)      # Output: int64 (or int32 depending on the system)

f_arr=np.array([2.4,2.5,8.4,4.5])

print(f_arr.dtype)