# # reduce() Function

# • reduce() is a Higher Order Function (HOF).

# • It takes another function as an argument.

# • It repeatedly applies the function to the elements of an iterable.

# • It reduces multiple values into a single value.

# • reduce() is available in the functools module.

# # Why is reduce() a HOF?

# A Higher Order Function is a function that:
# 1. Takes another function as an argument, OR
# 2. Returns a function.

# reduce() satisfies condition 1 because it accepts a function as an argument.

# # Syntax

# reduce(function, iterable)

# # Characteristics

# ✓ Produces a single output value
# ✓ Processes elements one by one
# ✓ Useful for calculations and aggregations
# ✓ Commonly used with lambda functions

# # Advantages

# ✓ Less code
# ✓ Efficient for cumulative operations
# ✓ Improves readability for simple aggregations

# # Interview Definition

# reduce() is a Higher Order Function that repeatedly
# applies a function to the elements of an iterable
# and reduces them to a single final value.


# sum of all item
import functools

# a=functools.reduce(lambda x,y:x+y, [1,2,3,4,6,7,3])
# print(a)

# # find min
# b=functools.reduce(lambda x,y:x if x<y else y ,[4,6,2,7,32,7,8])
# print(b)


# -----------------------------------------
# SUM OF ALL ELEMENTS USING reduce()
# -----------------------------------------

a = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 6, 7, 3])
print(a)

# Trace:

# Initial values:
# x=1, y=2  → 1+2 = 3

# Next:
# x=3, y=3  → 3+3 = 6

# Next:
# x=6, y=4  → 6+4 = 10

# Next:
# x=10, y=6 → 10+6 = 16

# Next:
# x=16, y=7 → 16+7 = 23

# Next:
# x=23, y=3 → 23+3 = 26

# Final Result = 26

# reduce() working:
# [1,2,3,4,6,7,3]
#  ↓
# (((((1+2)+3)+4)+6)+7)+3
#  ↓
# 26



# -----------------------------------------
# FIND MINIMUM ELEMENT USING reduce()
# -----------------------------------------

b = functools.reduce(
    lambda x, y: x if x < y else y,
    [4, 6, 2, 7, 32, 7, 8]
)

print(b)

# Logic:
# Compare two values at a time.
# Keep the smaller value and discard the larger one.

# Trace:

# x=4, y=6
# 4 < 6 → keep 4

# x=4, y=2
# 4 < 2 → False
# keep 2

# x=2, y=7
# 2 < 7 → keep 2

# x=2, y=32
# 2 < 32 → keep 2

# x=2, y=7
# 2 < 7 → keep 2

# x=2, y=8
# 2 < 8 → keep 2

# Final Result = 2

# reduce() working:
# [4,6,2,7,32,7,8]
#  ↓
# min(min(min(min(min(min(4,6),2),7),32),7),8)
#  ↓
# 2


# find max
print(functools.reduce(lambda x,y: x if x>y else y ,[434,67,45,4535,76,54])) 