# Q5`: Sort Dictionary key and values List.

# Input:
# {'c': [3], 'b': [12, 10], 'a': [19, 4]}

# Output:
# {'a': [4, 19], 'b': [10, 12], 'c': [3]}


ip={'c': [3], 'b': [12, 10], 'a': [19, 4]}

nd={}


s=sorted(ip.keys())

for i in s:
    nd[i]=ip[i]

print(nd)