# ==========================================
# Detect Missing Values (NaN)
# ==========================================

import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])


# np.isnan()
# Checks whether each element is NaN.
#
# Returns:
# True  -> Element is NaN.
# False -> Element is not NaN.

print(np.isnan(arr))

# Output:
# [False False  True False  True False]

# -----------------------------------------
# Why not use == to compare NaN?
# -----------------------------------------

# NaN follows the IEEE floating-point standard.
# According to this standard:
# A NaN value is NOT equal to any value,
# including another NaN.

# Therefore:
# np.nan == np.nan    -> False
# np.nan != np.nan    -> True

# Always use np.isnan() to detect NaN values,
# instead of using == or !=.

# Example:
# print(np.nan == np.nan)   # False
# print(np.isnan(np.nan))   # True