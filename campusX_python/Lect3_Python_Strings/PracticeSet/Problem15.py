# Problem 15: Removal of all characters from a string except integers
# Given:

# str1 = 'I am 25 years and 10 months old'
# Expected Output:

# 2510

str=input("Enter any string: ")

s=''
for i in str:
    if i>='0' and i<='9':
        s=s+i
print(s)