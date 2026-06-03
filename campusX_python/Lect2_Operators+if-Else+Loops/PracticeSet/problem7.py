# Reverse a given integer number

# Take a number as input from the user
num = int(input("Enter any no: "))

# rev will store the reversed number
# Initially it is 0
rev = 0

# i is used as the multiplier (10)
# Multiplying rev by 10 shifts its digits one place to the left
i = 10

# Repeat until all digits of num are processed num=0
while(num != 0):

    # Extract the last digit of num using num % 10
    # Shift the current rev one place left by multiplying by 10
    # Then add the extracted digit to rev

    rev = rev * i + num % 10

    # Remove the last digit from num
    # Example: 76542 becomes 7654

    num = num // 10

# Display the reversed number
print("Reverse: ",rev)


