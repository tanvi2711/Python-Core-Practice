# Types of Arguments

def power(a,b):
    return a**b


# x=(1)  # error
# x=power() 
x=power(1,2)
print(x)



# Default Argument

def power(a=2,b=2):  # a n b are defalut arguments
    return a**b

x=power()
print(x)



# Positional Argument

def power(a,b):    
    return a**b

x=power(6,2)  # 1 will  assign to a n 2 will assign to b it follows orderr 
print(x)


# Keyword Argument
def power(a,b):    
    return a**b

x=power(b=3,a=2)  # it dosnt follow position it will asign value in order that we send
print(x)




