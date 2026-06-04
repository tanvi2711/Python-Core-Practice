# Problem 12: Append second string in the middle of first string
# Input:

# campusx
# data
# Output:

# camdatapusx

str1=input("Enter any string: ")
str2=input("Enter any string: ")


s=str1[0:len(str1)//2]


s=s+str2


finalstr=s+str1[len(str1)//2-1:len(str1)]


print(finalstr)
