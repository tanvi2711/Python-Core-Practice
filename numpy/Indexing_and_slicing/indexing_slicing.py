import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 7, 8, 9])

print("--------------Indexing----------------")

print("--------1D--------")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[5])
print(arr[-1])

# Access the last element using the length of the array
print(arr[len(arr) - 1])

# Negative indexing starts from the end of the array
print(arr[-3])

print("--------2D--------")
arr2D = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

# Access element using [row, column]
print(arr2D[1, 3])

# Negative indexing for both row and column
print(arr2D[-1, -3])

print(arr2D[0, -3])
print(arr2D[0, 0])

print("--------------Slicing----------------")

print("--------1D--------")
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[0:])

# Syntax: array[start : stop : step]
print(arr[1:4:2])

# Slice till the second-last element with a step of 2
print(arr[:len(arr)-1:2])

# Exclude the last three elements
print(arr[:-3])

print("--------2D--------")
arr2D = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

# Slice columns from index 1 to 2 of the second row
print(arr2D[1, 1:3])

# Select all columns of the first row
print(arr2D[0, 0:])

# Select all columns except the last from the second row
print(arr2D[1, :-1])

# Slice from column 0 to 0 (returns an empty array)
print(arr2D[0, :0])

# Select alternate elements from columns 0 to 2
print(arr2D[0, 0:3:2])