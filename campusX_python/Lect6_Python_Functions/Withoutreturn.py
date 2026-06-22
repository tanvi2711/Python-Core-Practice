def is_even():
    num = input("Enter any no:")
    if type(num)==int:
        if num%2==0:
            # return f'{num} is even'
            print(f'{num} is even')
        else:
            # return f'{num} is odd'
            print(f'{num} is odd')
    else:
        print(f'{num} is not an interger ') 
    

print(is_even())


# it any fun didnt have  return statement then we can use print directly



print("#########################################")


# if function didnt have any return value or  print state it will return none 

def is_even():
    num = input("Enter any no:")
    if type(num)==int:
        if num%2==0:
            # return f'{num} is even'
            # print(f'{num} is even')
            pass
        else:
            # return f'{num} is odd'
            print(f'{num} is odd')
    else:
        print(f'{num} is not an interger ') 
    

print(is_even())

print("#########################################")

l=[1,2,3]
print(l.append(4))
print(l)