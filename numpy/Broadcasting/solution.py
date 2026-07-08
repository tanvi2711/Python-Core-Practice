# ==========================================
# NumPy Broadcasting
# ==========================================

"""
Broadcasting:
Broadcasting is a NumPy feature that allows arrays of
different shapes (or a scalar and an array) to perform
element-wise operations without explicitly making them
the same size.

It is automatic, fast, and memory efficient.
"""

import numpy as np

# -----------------------------------------
# Example: Apply a 10% Discount
# -----------------------------------------

prices = np.array([100, 200, 300, 400, 500, 600, 700, 800])

# Scalar value
discount = 10

print("Original Prices:")
print(prices)

print("\nDiscount:")
print(discount)

# -----------------------------------------
# Broadcasting
# -----------------------------------------

# Here, 'discount' is a scalar (single value).
# NumPy automatically broadcasts this scalar
# to every element of the 'prices' array.

# Internally, NumPy behaves as if:
#
# discount = [10, 10, 10, 10, 10, 10, 10, 10]
#
# IMPORTANT:
# This array is NOT actually created in memory.
# NumPy only behaves as if it exists.
# This makes broadcasting memory efficient.

# -----------------------------------------
# Backend Working
# -----------------------------------------

# Step 1:
# prices
# [100 200 300 400 500 600 700 800]

# Step 2:
# Broadcast the scalar 10
#
# [10 10 10 10 10 10 10 10]
#
# (Virtual expansion - not actually created)

# Step 3:
# Element-wise multiplication
#
# [100 200 300 400 500 600 700 800]
#               *
# [10  10  10  10  10  10  10  10]
#
# =
#
# [1000 2000 3000 4000 5000 6000 7000 8000]

# Step 4:
# Divide by 100
#
# [10 20 30 40 50 60 70 80]

# Step 5:
# Subtract discount from original prices
#
# [100 200 300 400 500 600 700 800]
#               -
# [10  20  30  40  50  60  70  80]
#
# =
#
# [90 180 270 360 450 540 630 720]

# -----------------------------------------
# Calculate Final Price
# -----------------------------------------

final_price = prices - (prices * discount / 100)

print("\nFinal Prices after 10% Discount:")
print(final_price)

# -----------------------------------------
# Broadcasting Rules
# -----------------------------------------

# Rule 1:
# If dimensions are equal -> Operation is allowed.

# Rule 2:
# If one dimension is 1 (or a scalar),
# NumPy stretches that dimension automatically.

# Rule 3:
# If dimensions are incompatible,
# NumPy raises a ValueError.

# -----------------------------------------
# Advantages of Broadcasting
# -----------------------------------------

# ✔ No loops required.
# ✔ Faster execution (implemented in optimized C code).
# ✔ Memory efficient.
# ✔ Cleaner and shorter code.
# ✔ Performs element-wise operations automatically.

# -----------------------------------------
# Interview Definition
# -----------------------------------------

# Broadcasting is the mechanism by which NumPy
# automatically expands the smaller array (or scalar)
# to match the shape of the larger array, allowing
# element-wise operations without creating unnecessary
# copies of data.