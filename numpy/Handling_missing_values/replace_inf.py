# ==========================================
# Replace Infinite Values (Inf)
# ==========================================

import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 6])

# np.isinf()
# Checks whether each element is
# positive or negative infinity.

print(np.isinf(arr))

# Output:
# [False False  True False  True False]

# -----------------------------------------
# Replace Infinite Values
# -----------------------------------------

# np.nan_to_num()
# Can also replace positive and negative
# infinity values.

# Syntax:
# np.nan_to_num(array, nan=value,
#               posinf=value,
#               neginf=value)

# Parameters:
# nan    -> Value to replace NaN.
# posinf -> Value to replace +Infinity.
# neginf -> Value to replace -Infinity.

# Important:
# - Returns a NEW array.
# - The original array remains unchanged.

# Replace:
# +Infinity -> 1000
# -Infinity -> -1000

cleaned_arr = np.nan_to_num(
    arr,
    posinf=1000,
    neginf=-1000
)

print(cleaned_arr)

# Output:
# [    1.     2.  1000.     4. -1000.     6.]

print()

# Original array remains unchanged
print(arr)

# Output:
# [  1.   2.  inf   4. -inf   6.]

# ==========================================
# Interview Point
# ==========================================

# np.nan_to_num() can replace:
# ✔ NaN values
# ✔ Positive Infinity (np.inf)
# ✔ Negative Infinity (-np.inf)
#
# making the data suitable for calculations
# and Machine Learning.