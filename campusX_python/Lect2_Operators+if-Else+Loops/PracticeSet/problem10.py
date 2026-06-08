# Problem 9: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.


# MY  LOGIC
# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,end=',')


# Create an empty list to store all valid numbers
nums = []

# Iterate through numbers from 2000 to 3200 (3201 is excluded)
for i in range(2000, 3201):

    # Check if the number is divisible by 7
    # and not divisible by 5
    if i % 7 == 0 and i % 5 != 0:

        # Convert the number to a string and
        # store it in the list
        # (join() works only with strings)
        nums.append(str(i))

# Combine all elements of the list into a single string,
# placing a comma between consecutive elements,
# and print the final comma-separated sequence
print(",".join(nums))





