# Problem 10: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a space-separated sequence on a single line.



# for i in range(1000,3001):
#     num=i
#     while(num!=0):
#         digit=num%10
#         if digit%2!=0:
#             break
#         num=num//10
#     if num==0:
#         print(i,end=' ')




# Iterate through all numbers from 1000 to 3000 (both included)
for i in range(1000, 3001):

    # Store the current number in a temporary variable
    # so that the original value of i remains unchanged
    num = i

    # Check each digit of the number one by one
    while(num != 0):

        # Extract the last digit of the number
        digit = num % 10

        # If the digit is odd, the number does not satisfy
        # the condition that all digits must be even
        if digit % 2 != 0:
            break

        # Remove the last digit and continue checking
        # the remaining digits
        num = num // 10

    # If num becomes 0, it means:
    # - Every digit was checked
    # - No odd digit was found
    # Therefore, all digits are even
    if num == 0:
        print(i, end=' ')