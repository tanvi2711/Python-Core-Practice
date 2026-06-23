# Q3:` Write a program to Check if a given string is binary string of or not. 

# A string is said to be binary if it's consists of only two unique characters.

# Take string input from user. 

# Input: str = "01010101010"
# Output: Yes

# Input: str = "1222211"
# Output: Yes

# Input: str = "Campusx"
# Output: No


b= input('Enter: ')

b_s=set()

for i in b:
    b_s.add(i)

if len(b_s)==2:
    print('Yes')
else:
    print("No")

