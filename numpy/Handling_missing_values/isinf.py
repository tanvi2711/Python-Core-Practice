# ==========================================
# Detect Infinite Values (Inf)
# ==========================================

import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

# np.inf  -> Positive Infinity
# -np.inf -> Negative Infinity

# Infinite values may occur due to operations like:
# - Division by zero.
# - Overflow in calculations.

# np.isinf()
# Checks whether each element is
# positive or negative infinity.

# Returns:
# True  -> Element is +inf or -inf.
# False -> Element is a finite number.

print(np.isinf(arr))

# Output:
# [False False  True False  True False]

# -----------------------------------------
# Important
# -----------------------------------------

# np.isinf() detects BOTH:
# ✔ Positive Infinity  (np.inf)
# ✔ Negative Infinity (-np.inf)

# It does NOT detect NaN values.
# Use np.isnan() to detect NaN.

# Example:
# print(np.isinf(np.inf))     # True
# print(np.isinf(-np.inf))    # True
# print(np.isinf(np.nan))     # False

# ==========================================
# Interview Definition
# ==========================================

# np.isinf() is used to check whether
# the elements of a NumPy array are
# positive or negative infinity.
# It returns a Boolean array containing
# True for infinite values and False
# for all finite values.