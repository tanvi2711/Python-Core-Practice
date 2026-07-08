# -----------------------------------------
# Filtering Data / Boolean Masking in NumPy
# -----------------------------------------

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Boolean Masking:
# A condition is applied to every element of the array.
# NumPy creates a Boolean array (True/False) of the same size.
# Elements with True are selected and returned.

# Important:
# Boolean masking returns a NEW array (copy), not a view.
# Modifying the filtered array will NOT change the original array.

# Select all elements greater than 5
# Condition: arr > 5
# Boolean Mask: [False False False False False True True True True]
# Result: [6 7 8 9]
print(arr[arr > 5])

# Select all even numbers
# Condition: arr % 2 == 0
# Boolean Mask: [False True False True False True False True False]
# Result: [2 4 6 8]
print(arr[arr % 2 == 0])