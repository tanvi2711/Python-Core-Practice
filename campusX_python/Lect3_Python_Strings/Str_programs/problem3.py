# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.


s=input("Enter any string: ")
term=input("Enter which words freqency u want: ")

f=0

for i in s:
    if i==term:
        f+=1

print(f"Frequency of {term} in this string is {f}")
