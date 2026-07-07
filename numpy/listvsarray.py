# python_list=[1,2,3,4,5,6]
# print(python_list)

# import numpy as np

# numpy_array=np.array([1,2,3,4,5,6])
# print(numpy_array)


# ==========================================
# Python List vs NumPy Array
# ==========================================

# Python List
# - Built-in Python data structure.
# - Can store different data types.
# - Slower for numerical calculations.
# - Uses more memory because each element is stored as a separate Python object.

python_list = [1, 2, 3, 4, 5, 6]
print("Python List :", python_list)

# Import NumPy library
import numpy as np

# NumPy Array
# - Created using np.array().
# - Stores elements of the same data type (homogeneous).
# - Faster and more memory-efficient.
# - Stores data in contiguous (continuous) memory locations.
# - Requires less memory than Python lists.
# - Best for mathematical operations and large datasets.
# - Widely used in Data Science, AI, and Machine Learning.

numpy_array = np.array([1, 2, 3, 4, 5, 6])
print("NumPy Array :", numpy_array)

# Memory Difference:
# Python List  -> More memory usage (stores references to objects).
# NumPy Array  -> Less memory usage (stores values in contiguous memory).

# Use Python List  -> General-purpose programming.
# Use NumPy Array  -> Numerical computing and large datasets.