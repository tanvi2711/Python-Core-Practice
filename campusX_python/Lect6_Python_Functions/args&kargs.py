# *args and **kwargs

# *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function


# *args
# allows us to pass a variable number of non-keyword arguments to a function.

def multiply(a,b,c):
    return(a*b*c)

print(multiply(2,3,3))

print("############################################")

# Now we want multiple num in parameters so will use *args means we can send any no of values it will accept

def multiply(*args):
# def multiply(*salman):
    product=1

    # for i in salman:
    for i in args:
        product=product*i

    return product

print(multiply(2,3,3,3,2,2,4,4))  # args store it in tuple n use that in function
print(multiply(2,3,2,2,4,4))
print(multiply(2,3))
print(multiply(2))

print("##########################################")
# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key ,"-->",value)

print(display(India='delhi',Srilanka='colombo',Nepal='Kathmandu'))
