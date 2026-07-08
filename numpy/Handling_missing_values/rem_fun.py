# ==========================================
# NumPy Functions that Ignore NaN Values
# ==========================================

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

# These functions ignore NaN values while
# performing calculations.

# -----------------------------------------
# np.nanmean()
# -----------------------------------------

# Calculates the average while ignoring NaN values.

print(np.nanmean(arr))

# Output:
# 3.25

# -----------------------------------------
# np.nansum()
# -----------------------------------------

# Calculates the sum while ignoring NaN values.

print(np.nansum(arr))

# Output:
# 13.0

# -----------------------------------------
# np.nancumsum()
# -----------------------------------------

# Calculates the cumulative sum while treating
# NaN values as 0.

# Cumulative Sum:
# [1, 3, 3, 7, 7, 13]

print(np.nancumsum(arr))

# Output:
# [ 1.  3.  3.  7.  7. 13.]

# -----------------------------------------
# np.nanmin()
# -----------------------------------------

# Returns the smallest value while
# ignoring NaN values.

print(np.nanmin(arr))

# Output:
# 1.0

# -----------------------------------------
# np.nanmax()
# -----------------------------------------

# Returns the largest value while
# ignoring NaN values.

print(np.nanmax(arr))

# Output:
# 6.0

# ==========================================
# Why use these functions?
# ==========================================

# Regular functions like:
# np.mean()
# np.sum()
# np.min()
# np.max()
#
# may return NaN if the array contains NaN values.

# The "nan" versions ignore missing values
# and produce meaningful results.

# ==========================================
# Interview Point
# ==========================================

# Functions starting with "nan" ignore
# missing values (NaN) while performing
# mathematical operations.