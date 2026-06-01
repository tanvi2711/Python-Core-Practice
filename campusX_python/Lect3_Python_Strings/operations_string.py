# arithmatic operation 
print("-------------arithmatic operation------------------")
print('mumbai'+'delhi')
print('mumbai'+' '+'delhi')
print('delhi'*5)
print("*"*5)


# relational operation
print("---------------relational operation------------------")
print("delhi"=="delhi")
print("mumbai"=="delhi")
print('mumbai'>'pune')  #lexiographically comapre means comparision based on ascii values
print('Pune'>'pune')

# logical operation
print("----------------logical operation-------------------")
print('hello' and 'world')  
print('hello' or 'world') 
# in python if any string have characters in it it will consider as TRUE n if any string is EMPTY it will consider as FALSE

print("" and 'World') #false
print("" or 'World')
print(not '')
print(not 'hello')


#Loops on Strings
print("----------------Loops on Strings-------------------") 
for i in 'hello':
    print(i)

for i in 'delhi':
    print('pune')

# Membership Operations
print("---------------Membership Operations-----------------")
print('D'in 'delhi')
print('D'in 'Delhi')
print('M'not in'delhi')

