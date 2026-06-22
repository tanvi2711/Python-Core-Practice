# # GLOBAL VARIABLE VS LOCAL VARIABLE 

# def g(y):    # this is in function scope  y is local variable 
#     print(x)
#     print(x+1) 

# x = 5      # this is in program scope x is global variable 
# g(x)   
# print(x)  

# local cant use global but global can use local
# ex in above program global variable x is in function so x is used by local variablr y



# # Global var n local var cana have same name but it totally work independently
# def f(y):   # this is in function scope  y is local variable 
#     x = 1       # this is in function scope  x is local variable 
#     x += 1
#     print(x)

# x = 5  # this is in program scope x is global variable 
# f(x) 
# print(x)

# # there is no relation btw global variable x n local variable x 

# # It will give error 
# def h(y):
#     x += 1  # x is global vaiable n it is used in function scope 
# x = 5  #global var
# h(x)
# print(x)


# still we have to do same we can do it like this but this is not a good practice 
# def h(y):
#     global x
#     x += 1  
# x = 5 
# h(x)
# print(x)


def f(x):
   x = x + 1  #local variable 
   print('in f(x): x =', x)
   return x

x = 3  # global variable 
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)




# Variable Scope

# Scope defines where a variable
# can be accessed.

# Global Variable
# - Declared outside a function.
# - Accessible throughout the program.

# Local Variable
# - Declared inside a function.
# - Accessible only within that function.

# global Keyword
# - Used to modify a global variable
#   inside a function.