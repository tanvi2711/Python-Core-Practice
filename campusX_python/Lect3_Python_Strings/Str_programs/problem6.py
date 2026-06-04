# Write a program to count the number of words in a string without split()

s = input('enter the string: ')

count=0

for i in s:
    if i==' ':
        count+=1

print(f"In {s} there are {count+1} words")


# s = input('enter the string')
# L = []
# temp = ''
# for i in s:

#   if i != ' ':
#     temp = temp + i
#   else:
#     L.append(temp)
#     temp = ''

# L.append(temp)
# print(L)

