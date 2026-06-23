# Q4`: Convert a list of Tuples into Dictionary.

# Input:
# [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]

# Output:
# {'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}


d=[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]

k={}


for i in d:
    k[i[0]]=[i[1]]

print(k)