# Problem 5 - Exercise 12: Display Fibonacci series up to 10 terms.
# Note: The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34



# Take input from the user for the number of Fibonacci terms to display
num = int(input("Enter nth term: "))

# Print the first two Fibonacci numbers
print(0, " ", end='')
print(1, " ", end='')

# m stores the first previous Fibonacci number
# n stores the second previous Fibonacci number
# Initially, the sequence starts with 0 and 1
m = 0
n = 1

# Generate the remaining Fibonacci terms
for i in range(1, num - 1):

    # The next Fibonacci number is obtained
    # by adding the previous two numbers (m and n)
    k = m + n

    # Display the newly generated Fibonacci number
    print(k, " ", end='')

    # Shift the values forward:
    # The current value of n becomes the new m
    m = n

    # The newly generated Fibonacci number k becomes the new n
    n = k

    # Example:
    # Initially: m = 0, n = 1
    # k = 0 + 1 = 1
    # Update: m = 1, n = 1
    #
    # Next iteration:
    # k = 1 + 1 = 2
    # Update: m = 1, n = 2
    #
    # Next iteration:
    # k = 1 + 2 = 3
    # Update: m = 2, n = 3