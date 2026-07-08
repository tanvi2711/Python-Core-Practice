import numpy as np

print("--------------Reshape----------------")

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

# reshape():
# Changes the shape (dimensions) of an array
# without changing its data.

# Syntax:
# array.reshape(rows, columns)

# Important:
# - Total number of elements must remain the same.
# - reshape() returns a new array with the desired shape.
# - The original array remains unchanged.
# - If the shape is incompatible, NumPy raises a ValueError.

reshaped_arr = arr.reshape(3, 3)

print(reshaped_arr)

print()

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

reshaped_arr=arr.reshape(5,2)
print(reshaped_arr)

print()


# Reshape the 1D array into a 5 x 2 array
print(arr.reshape(5, 2))

print()

# Original array is still 1D
print(arr)

# Output:
# Reshaped Array:
# [[ 10  20]
#  [ 30  40]
#  [ 50  60]
#  [ 70  80]
#  [ 90 100]]
#
# Original Array:
# [10 20 30 40 50 60 70 80 90 100]

# print(reshaped_arr)









