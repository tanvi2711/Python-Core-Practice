# Problem 20: Write a program that can remove all the duplicate characters from a string. User will provide the input.

str=input("Enter any string: ")

s=''


for ch in str:  
    if ch not in s:
        s+=ch

print(s)

