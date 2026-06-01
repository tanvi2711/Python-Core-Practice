s=input("Enter any string: ")

# Common Functions
# len
# max
# min
# sorted

print("Length: ",len(s))
print("Max: ",max(s))
print("Min: ",min(s))
print("Sorted: ",sorted(s))
print("Reverse Sorted: ",sorted(s,reverse=True))


# Capitalize/Title/Upper/Lower/Swapcase
print("Capitalize: ",s.capitalize())
print("Title: ",s.title())
print("Lower: ",s.lower())
print("Swapcase: ",s.swapcase())


# Count/Find/Index
print("Count how many time 'l' apper in string: ",s.count('l'))
print("Find where is 'is' in the sentence: position[",s.find('is'),']')
print("Find where is 'x' in the sentence: position[",s.find('x'),']')

print("Find where is 'is' in the sentence: position[",s.index('is'),']')
# print("Find where is 'x' in the sentence: position[",s.index('x'),']') show error


# endswith/startswith
print(s.endswith('Jivatode'))
print(s.endswith('nvi'))

print(s.startswith('Jivatode'))
print(s.startswith('my'))

# format
name='Tanvi'
gender='Engg'
str='My name is {} and I am {}'
print(str.format(name,gender))
str='My name is {1} and I am {0}'
print(str.format(name,gender))

#  isalnum/ isalpha/ isdigit/ isidentifier
print("Is string contain no? : ",s.isalnum())
print("Is string 'Tanvi987999' contain no? : ",'Tanvi987999'.isalnum())

print("Is string contain characters only? : ",s.isalpha())
print("Is string 'Tanvi987999' contain characters only? : ",'Tanvi987999'.isalpha())
print("Is string 'Tanvi' contain characters only? : ",'Tanvi'.isalpha())

print("Is string contain digits only? : ",s.isdigit())
print("Is string '123' contain digits only? : ",'123'.isdigit())
print("Is string 'tanvi124' contain digits only? : ",'tanvi124'.isdigit())

print("Is string is identifier? : ",s.isidentifier())
print("Is string 'tanvi' is identifier? : ",'tanvi'.isidentifier())
print("Is string 'Tanvi' is identifier? : ",'Tanvi'.isidentifier())
print("Is string '1Tanvi' is identifier? : ",'1Tanvi'.isidentifier())


# Split/Join
print(s.split())
print(s.split('i'))

print('-'.join(s))

# replace
print(s.replace('Tanvi' , 'tanvi'))

# strip
print('Tanvi                 '.strip())