# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh


s=input("Enter any email: ")

for i in s:
    if i=='@':
        break
    else:
        print(i,end='')


# slicing logic
# pos=s.index('@')

# print(s[0:pos])