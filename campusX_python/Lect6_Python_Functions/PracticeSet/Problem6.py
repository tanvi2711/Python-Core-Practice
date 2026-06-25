# Problem-6: Write a Python function to concatenate any no of dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


def dict_con(d,*args):
    for i in args:
        for j in i:
            d[j]=i[j]
    return d


print(dict_con({},{1:10, 2:20},{3:30, 4:40},{5:50,6:60}))