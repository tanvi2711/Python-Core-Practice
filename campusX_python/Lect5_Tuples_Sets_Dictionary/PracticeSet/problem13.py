# Q3`: Convert List to List of dictionaries. Given list values and keys list, convert these values to key value pairs in form of list of dictionaries.

# Input:
# test_list = ["DataScience", 3, "is", 8]
# key_list = ["name", "id"]

# Output:
# [{'name': 'DataScience', 'id': 3}, {'name': 'is', 'id': 8}]


test_list = ["DataScience", 3, "is", 8]
key_list = ["name", "id"]

d=[]

k={}

for i in key_list:
    for j in test_list:
        print(i)
        
        if i not in k:
            k[i]=j
            print(k[i],k)
    d.append(k)

print(d)