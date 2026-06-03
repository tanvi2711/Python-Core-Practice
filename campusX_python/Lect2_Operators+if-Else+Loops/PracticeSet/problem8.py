# Problem 8: Take a user input as integer N. Find out the sum from 1 to N. If any number if divisible by 5, then skip that number. And if the sum is greater than 300, don't need to calculate the sum further more. Print the final result. And don't use for loop to solve this problem.
# Example 1:

# Input:

# 30
# Output:

# 276


# Take the upper limit (N) from the user
num = int(input("Enter any no: "))

# Variable to store the running sum
sum = 0

# Counter variable starting from 1
i = 1

# Iterate from 1 to N using a while loop
while(i <= num):

    # Skip numbers that are divisible by 5
    # They should not be included in the sum
    if i % 5 == 0:
        i += 1          # Move to the next number
        continue        # Skip the rest of the current iteration

    # Before adding the current number,
    # check whether it would make the sum exceed 300.
    # If yes, stop the loop immediately.
    if sum + i > 300:
        break

    # Add the current number to the running total
    sum = sum + i

    # Move to the next number
    i += 1

# Display the final result
print("Sum of", num, "is:", sum)