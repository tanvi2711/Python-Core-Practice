# Problem 5:Write a Python function to check whether a number is perfect or not.

# A Perfect number is a number that is half the sum of all of its positive divisors (including itself).


# The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. 
# Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. 

# The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.


# def is_perfect(n):
#     s=n
#     for i in range(1,n):
#         s=s+i
#         if s/2==n and s!=2:
#             return True


def is_perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
        if s/2==n and s!=2:
            return True
        

x=int(input("Enter any no:"))
is_perfect(x)


if is_perfect(x)==True:
    print(f"{x} is a prefect number")
else:
    print(f"{x} is a not prefect number")

