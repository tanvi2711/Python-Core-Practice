# -----------------------------------------
# Insert Rows and Columns in a 2D Array
# -----------------------------------------

import numpy as np

arr2d = np.array([[10, 20, 30],
                  [40, 50, 60]])

# -----------------------------------------
# Insert a Row
# -----------------------------------------

# axis = 0 -> Row-wise insertion.
# The list [70, 80, 90] becomes a new row.
# It is inserted at row index 2.

# Original:
# [[10 20 30]
#  [40 50 60]]
#
# Result:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]

arr2D_final = np.insert(arr2d, 2, [70, 80, 90], axis=0)

print(arr2D_final)

print()

# -----------------------------------------
# Insert a Column
# -----------------------------------------

# axis = 1 -> Column-wise insertion.
# The list [70, 80] becomes a new column.
# 70 is inserted into the first row.
# 80 is inserted into the second row.
# The column is inserted at column index 2.

# Original:
# [[10 20 30]
#  [40 50 60]]
#
# Result:
# [[10 20 70 30]
#  [40 50 80 60]]

arr2D_new = np.insert(arr2d, 2, [70, 80], axis=1)

print(arr2D_new)


# Original array remains unchanged
