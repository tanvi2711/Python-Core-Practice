# # filter() Function

# • filter() is a Higher Order Function (HOF).

# • It takes another function as an argument.

# • It checks each element of an iterable based on a condition.

# • Only elements that satisfy the condition are kept.

# • Returns a filter object containing the filtered values.

# # Why is filter() a HOF?

# A Higher Order Function is a function that:
# 1. Takes another function as an argument, OR
# 2. Returns a function.

# filter() satisfies condition 1 because it accepts a function as an argument.

# # Syntax

# filter(function, iterable)

# # Advantages

# ✓ Less code
# ✓ Easy filtering of data
# ✓ Improves readability
# ✓ Commonly used with lambda functions

# # Interview Definition

# filter() is a Higher Order Function that applies a
# condition to each item of an iterable and returns
# only those elements that satisfy the condition.


# numbers greater than 5
L = [3,4,5,6,7]
a=filter(lambda x: x>5,L)
for i in list(a):
    print(i)


# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']
b=filter(lambda x:'a' in x , fruits)
for i in list(b):
    print(i)