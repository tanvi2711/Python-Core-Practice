def is_even1(n):   # here n is parameter 
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
    x=is_even1(i) # i is argument when fun is called n any value is passed to it it called as argument
    print(x)
