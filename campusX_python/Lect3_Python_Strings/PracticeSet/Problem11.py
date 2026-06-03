# Problem 11: Create Short Form from initial character
# Given a string create short form ofthe string from Initial character. Short form should be capitalised.

# Example:

# Input:

# Data science mentorship program
# Output:

# DSMP

str=input("Enter any string: ")

s=str.title()


for i in s:
    if i>='A' and i<='Z':
        print(i,end='')

