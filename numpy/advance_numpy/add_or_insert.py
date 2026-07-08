"""
-----------------------------------------
NumPy insert()
-----------------------------------------

Syntax:
np.insert(array, index, values, axis=None)

Parameters:
array  -> Original NumPy array.
index  -> Position where the new value(s) will be inserted.
values -> Value or values to insert.
axis   -> Specifies where insertion takes place.

axis = None (default)
    - Array is treated as a 1D (flattened) array.
    - Returns a new 1D array.

axis = 0
    - Insert row(s) in a 2D array.

axis = 1
    - Insert column(s) in a 2D array.

Important:
- np.insert() DOES NOT modify the original array.
- It creates and returns a NEW array with the inserted value(s).
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Insert 25 at index 2
# Original : [10 20 30 40 50 60]
# Result   : [10 20 25 30 40 50 60]
new_arr = np.insert(arr, 2, 25)

print(new_arr)

# axis=0 has the same effect for a 1D array
# because there is only one axis.
new_arr = np.insert(arr, 2, 25, axis=0)

print(new_arr)

# Original array remains unchanged
print(arr)