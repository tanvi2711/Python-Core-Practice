# Problem 10:` Add Space between Potential Words.

# **Example:**

# Input:
# ['campusxIs', 'bestFor', 'dataScientist']

# Output:
# ['campusx Is', 'best For', 'data Scientist']

l=['campusxIs', 'bestFor', 'dataScientist']

s=''

l1=[]

for i in l:
    for j in i:
        if j>='A' and j<='Z':
            s=s+' '    
        s=s+j
    l1.append(s)
    s=''
print(l1)