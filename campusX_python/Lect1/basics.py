# Print 
print("-------------PRINT-------------")

print("Hello, World")
print(123)
print('Hello',1,2,3,True)   
print('Hello',1,2,3,True,sep='/')
print('Hello',end='-')
print("World")


# Data Types

# int
print("-------------INT-------------")
print(8)
print(1e308)
print(1e309)

# float
print("-------------FLOAT-------------")
print(8.66)
print(1.7e300)
print(1.7e309)


# boolean
print("-------------BOOLEAN-------------")
print(True)
print(False)


# string
print("-------------STRING-------------")
print("Hello, World")

# complex no
print("-------------complexno-------------")
print(5+6j)


# list
print("-------------LIST-------------")
print([1,2,3,4])

# tuple
print("-------------TUPLE-------------")
print((1,2,3,4))


# sets
print("-------------SETS-------------")
print({1,2,3,4,5})

# dict
print("-------------DICT-------------")
print({'Name':'Tanvi','Gender': 'Female', 'weight': 55})


# Type 
print("-------------type-------------")
print(type(3))
print(type(3.3))
print(type(3+5j))


################Dynamic typing###################
# while creating variable we didnt mention data type in python while in other lang we mention datat type as int char ,etccc this concept is called dynamic typing 
a=5  

# static typing 
# int a =5 

# Dynamic Binding (IF WE CREATE ONE VARIABLE WE CAN USE IT AS ANY DATA TYPE THEIR IS NO FIX DATAT TYPE TO IT IN OTHER LANG IF WE DEFINE ANY VARIABLE AS INT IT WILL BE OF INT DATA TYPE THROUGHOUT THE PROG)
print("-------------Dynamic Binding-------------")
a=5
print(a)
a='tanvi'
print(a)  


# Multiple variables are initialized in one line
print("Multiple variables are initialized in one line")
a,b,c=1,2,3
print(a,b,c)


# Multiple variables asign same value
print("Multiple variables asign same value")
a=b=c=5
print(a,b,c)


# Keywords 
# in python there are 32 keywords

# identifiers
# variable name function name class names these all are called as identifiers 

# we can use _ as a identifier
_=5
print(_)


# static s/w = information type website
# dynamic s/w = having some use n user will interact with it

print("-------------userinput -------------")
input("Enter ur name : ") #string
int(input("enter any no : " ))   #number
 
# Type Conversion
print("-------------Type Conversion-------------")

print("Implicit")
print(5+6.4)
print(type(5),type(5.6))
# print(4+'5') not possible 


print("Explicit")
print(int('4'))
print(int(4.9))
# print(int(4+5j)) not possible
print(str(5))
print(float('4'))


# python type conversion doesnot chage data type of variabke it created new datat only 
print("python type conversion doesnot chage data type of variabke it created new data only")
num='1'
print(int(num))
print(type(num))


# Literals 
print("-------------Literals---------------")
a=0b1010 #0b indicates binary (it is a binary literal)
print(a)
b=100 #Decimal literal
print(b)
c=0o310 # octal literal
print(c)
d=0x12c # hexadecimal literal
print(d)

# float literal
float_1=10.5
float_2=1.5e2 #1.5*10^2
print(float_2)
float_3=1.5e-3 # 1.5*10^-3
print(float_3)

# complex literals 
x=3+3.14j
print(x.real,x.imag)

# Unicode 
print("----------Unicode-------------")
unicode=u"\U0001f600\U0001f606"
print(unicode)


# Boolean
print("----------BOOLEAN----------")
a=True +4  # True = 1
b=False +10   # False=0
print("a:" ,a)
print("b:" ,b)


# None
print("------None-------")
a=None
print(a)


# /Use of none
k=None 
a=5
b=5
print("Prog exe")