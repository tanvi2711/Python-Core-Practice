# Write a program to check whether a given string is a palindrome or not.
# A palindrome reads the same from left to right and right to left.
# Examples:
# abba -> Palindrome
# malayalam -> Palindrome
# hello -> Not Palindrome

# Take string input from the user
s = input('enter the string: ')

# 'a' points to the last character of the string
a = len(s) - 1

# 'b' points to the first character of the string
b = 0

# Variable to store palindrome status
palindrom = 0

# Traverse the string
for i in s:

    # Compare characters from both ends
    if s[b] != s[a]:

        # If characters don't match, string is not a palindrome
        print(f"{s} is not palindrom string")

        # Update flag and stop checking further
        palindrom = False
        break

    else:

        # Move the pointers towards the center
        a -= 1
        b += 1

        # Characters matched so far
        palindrom = True

# If all compared characters matched, string is a palindrome
if palindrom == True:
    print(f"{s} is palindrom string")