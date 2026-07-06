# Given a list of numbers, the task is to print all positive numbers in the list. A positive number is any number greater than 0.

# For example:

# a = [-10, 15, 0, 20, -5, 30, -2] 
# Positive numbers = 15, 20, 30

a = [-10, 15, 0, 20, -5, 30, -2] 

x=filter(lambda x: x>0,a)
print(list(x))