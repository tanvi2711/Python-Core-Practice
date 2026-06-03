# Problem 12: Append second string in the middle of first string
# Input:

# campusx
# data
# Output:

# camdatapusx

str1=input("Enter any string: ")
str2=input("Enter any string: ")

length=len(str1)


s=str1[0:length//2]


s=s+str2


finalstr=s+str1[length//2-1:length]


print(finalstr)
