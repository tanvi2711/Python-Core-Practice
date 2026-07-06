# Example:

# Input: lst = [12, -7, 5, 64, -14]
# Output: -7, -14

a = [12, -7, 5, 64, -14] 

x=filter(lambda x: x<0,a)
print(list(x))