# # map() Function

# • map() is a Higher Order Function (HOF).

# • It takes another function as an argument.

# • It applies that function to every element of an iterable
#   (list, tuple, set, etc.).

# • Returns a map object containing transformed values.

# # Why is map() a HOF?

# A Higher Order Function is a function that:
# 1. Takes another function as an argument, OR
# 2. Returns a function.

# map() satisfies condition 1 because it accepts a function as an argument.

# # Syntax

# map(function, iterable)

# # Advantages

# ✓ Less code
# ✓ Faster than traditional loops
# ✓ Improves readability
# ✓ Commonly used with lambda functions

# # Interview Definition

# map() is a Higher Order Function that applies a given
# function to each item of an iterable and returns the
# transformed results.

# square the items of a list
a=map(lambda x:x**2,[1,2,3,4,5,6])
print(list(a))

# odd/even labelling of list items
b=map(lambda x: f'{x} is even' if x%2==0 else f'{x} is odd' ,[1,2,3,4,5,6,7,8,9])
for i in list(b):
    print(i)


# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

c=map(lambda users:users['name'],users)
for i in list(c):
    print(i)

