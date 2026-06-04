# Write a program which can remove a particular character from a string.


s = input('enter the string: ')
term = input('what would like to remove: ')

result=''
print(s[1])

for i in s:
    if i!=term:
        result+=i

print(result)