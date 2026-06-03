# # Problem 6 - Find the factorial of a given number.
# # Write a program to use the loop to find the factorial of a given number.

# # The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

# # For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Output:

# 120

num=int(input("Enter any no: "))

fact=1
for i in range(1,num+1):
    fact=fact*i
print("Fctorial of",num,"is: ",fact)