# ==============================================================================
#                    NumPy Array Creation Methods
# ==============================================================================

import numpy as np

# ------------------------------------------------------------------------------
# np.array()
# ------------------------------------------------------------------------------
# Used to create a NumPy array from a Python list, tuple, or other iterable.
#
# Syntax:
# np.array(object, dtype=None)
#
# Parameters:
# object -> List, Tuple, etc. (Required)
# dtype  -> Data type of elements (Optional)
#
# Returns:
# A NumPy ndarray (N-dimensional array)
# ------------------------------------------------------------------------------

arr = np.array([1, 2, 3, 4, 5, 6, 7, 7])
print(arr)


# ------------------------------------------------------------------------------
# np.zeros()
# ------------------------------------------------------------------------------
# Used to create an array where every element is 0.
#
# Syntax:
# np.zeros(shape, dtype=float)
#
# Parameters:
# shape -> Number of elements or rows & columns (Required)
# dtype -> Data type (Optional, default=float)
#
# Returns:
# An array filled with zeros.
#
# Common Uses:
# • Initialize arrays
# • Machine Learning
# • Image Processing
# ------------------------------------------------------------------------------

arr = np.zeros(5)
print(arr)


# ------------------------------------------------------------------------------
# np.ones()
# ------------------------------------------------------------------------------
# Used to create an array where every element is 1.
#
# Syntax:
# np.ones(shape, dtype=float)
#
# Parameters:
# shape -> Array dimensions (Required)
# dtype -> Data type (Optional)
#
# Returns:
# An array filled with ones.
# ------------------------------------------------------------------------------

ones_arr = np.ones((2, 4))
print(ones_arr)


# ------------------------------------------------------------------------------
# np.full()
# ------------------------------------------------------------------------------
# Used to create an array filled with a specific value.
#
# Syntax:
# np.full(shape, fill_value, dtype=None)
#
# Parameters:
# shape      -> Array dimensions (Required)
# fill_value -> Value to fill (Required)
# dtype      -> Data type (Optional)
#
# Returns:
# An array where every element contains the given value.
# ------------------------------------------------------------------------------

full_arr = np.full((2, 3), 7)
print(full_arr)


# ------------------------------------------------------------------------------
# np.arange()
# ------------------------------------------------------------------------------
# Used to generate a sequence of evenly spaced numbers.
#
# Syntax:
# np.arange(start, stop, step)
#
# Parameters:
# start -> Starting value (Optional, default=0)
# stop  -> Ending value (Required, not included)
# step  -> Increment value (Optional, default=1)
#
# Returns:
# A NumPy array containing evenly spaced values.
# ------------------------------------------------------------------------------

seq = np.arange(1, 10, 2)
print(seq)


# ------------------------------------------------------------------------------
# np.eye()
# ------------------------------------------------------------------------------
# Used to create an Identity Matrix.
#
# Identity Matrix:
# A square matrix in which all diagonal elements are 1
# and all remaining elements are 0.
#
# Syntax:
# np.eye(N, M=None, k=0, dtype=float)
#
# Parameters:
# N -> Number of rows (Required)
# M -> Number of columns (Optional, default=N)
# k -> Diagonal index (Optional, default=0)
#
# Returns:
# An Identity Matrix.
#
# Common Uses:
# • Linear Algebra
# • Matrix Calculations
# • Machine Learning
# • Deep Learning
# ------------------------------------------------------------------------------

identity_matrix = np.eye(3)
print(identity_matrix)

print()

identity_matrix = np.eye(4)
print(identity_matrix)