# Problem 16: Check whether the string is Symmetrical.
# Statement: Given a string. the task is to check if the string is symmetrical or not. A string is said to be symmetrical if both the halves of the string are the same.

# Example 1:

# Input

# khokho
# Output

# The entered string is symmetrical

str=input("Enter any string: ")

l=len(str)


if str[0:l//2]==str[l//2:l]:
    print(str," is symmetrical string")
else:
    print(str," is not symmetrical string")