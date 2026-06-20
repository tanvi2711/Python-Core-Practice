# Problem 7:` Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.

# `Input:
# ['1ac21', '23fg', '456', '098d','1','kls']

# `Output:
# ['456', '23fg', '1ac21', '1', 'kls', '098d']

l=['1ac21', '23fg', '456', '098d','1','kls']

l1=[]
p=[]


for i in l:
    product=1
    for j in i:
        if j.isdigit():
            product*=int(j)
    l1.append(i)
    l1.sort()
print(l1)
