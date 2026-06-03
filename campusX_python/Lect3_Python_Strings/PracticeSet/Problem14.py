# Problem 14:Take a alphanumeric string input and print the sum and average of the digits that appear in the string, ignoring all other characters.
# Input:

# hel123O4every093

# Output:

# Sum: 22
# Avg: 2.75


str=input("Enter any string: ")
sum=0
count=0

for i in str:
    if i>='0' and i<='9':
        sum=sum+int(i)
        count+=1

print("Sum: ",sum)
print("Avg:",sum/count)