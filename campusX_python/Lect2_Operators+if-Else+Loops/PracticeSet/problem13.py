# Problem 12:Write a program to print whether a given number is a prime number or not

num=int(input("Enter any no: "))

if num <= 1:
    print(num, "is not prime")

else:
    for i in range(2, num):

        # If any number divides num exactly,
        # then num is not prime
        if num % i == 0:
            print(num, "is not prime")
            break

    # Executes only if the loop never breaks
    else:
        print(num, "is prime")