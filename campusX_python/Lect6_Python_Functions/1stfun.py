# def is_even():
#     """
#     This function returns if a given number is odd or even
#     input - any valid integer
#     output - odd/even
#     created on - 16th Nov 2022
#     """
    
#     num = int(input("Enter any no:"))
#     if num%2==0:
#         return f'{num} is even'
#     else:
#         return f'{num} is odd'
    
# x=is_even()

# print(x)



def is_even1(n):
    """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    created on - 16th Nov 2022
    """
    if n%2==0:
        return f'{n} is even'
    else:
        return f'{n} is odd'
    
for  i in range(1,11):    
    x=is_even1(i)
    print(x)



print("################################################")



def is_even():
    """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    created on - 16th Nov 2022
    """
    
    num = input("Enter any no:")
    if type(num)==int:
        if num%2==0:
            return f'{num} is even'
        else:
            return f'{num} is odd'
    else:
        return f'{num} is not an interger '
    
x=is_even()

print(x)


# how to featch documentation of function
print(is_even.__doc__)

print(print.__doc__)