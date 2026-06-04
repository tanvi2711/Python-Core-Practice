# Write a program that can convert an integer to string.

number = int(input('enter the number: '))

# String containing all digit characters
digits = "0123456789"

# Initialize an empty string to store the result
result = ""

# Convert the integer to a string digit by digit
while number != 0:
    # Extract the last digit and append its character representation
    result = digits[number % 10] + result

    # Remove the last digit from the number
    number = number // 10

# Display the converted string
print(result)

print(type(result))