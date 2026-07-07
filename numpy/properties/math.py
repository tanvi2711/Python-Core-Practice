# ------------------------------------------------------------------------------
# Arithmetic Operations on NumPy Arrays
# ------------------------------------------------------------------------------
# NumPy allows mathematical operations to be performed directly on arrays.
# These operations are applied to every element of the array.
#
# Supported Operators:
# +  -> Addition
# -  -> Subtraction
# *  -> Multiplication
# /  -> Division
# ** -> Exponent (Power)
# %  -> Modulus
#
# Benefits:
# • No loops required (Vectorization)
# • Faster execution
# • Cleaner and shorter code
# • Efficient for large datasets
# ------------------------------------------------------------------------------

import numpy as np

# Create a NumPy array
arr = np.array([12, 54, 23])

# Add 5 to each element
print(arr + 5)      # Output: [17 59 28]

# Multiply each element by 2
print(arr * 2)      # Output: [24 108 46]

# Square each element (power of 2)
print(arr ** 2)     # Output: [144 2916 529]

# Cube each element (power of 3)
print(arr ** 3)     # Output: [1728 157464 12167]

# import numpy as np
# arr=np.array([12,54,23])

# print(arr+5)
# print(arr*2)
# print(arr**2)
# print(arr**3)