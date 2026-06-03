# Problem 13:Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:

# str1 = PyNaTive

# Expected Output:

# yaivePNT

str=input("Enter any string: ")

s1=''
s2=''


for i in str:
    if i>='a' and i<='z':
        s1=s1+i
    if i>='A' and i<='Z':
        s2=s2+i
print(s1+s2)