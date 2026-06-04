# Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.

str=input("Enter any string: ")
s=''
for i in range(0,len(str)):
    # if str[i]==str[i+1] or :
        print(i,i+1)
        s=str.replace(str[i],str[i+1])
print(s)
        