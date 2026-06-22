# HOF is a function in which it retrun another function or a function which receive another function as input 


def sqr(x):
    return x**2

def cube(x):
    return x**3

# HOF
def transform(f,l):
    output=[]
    for i in l:
        output.append(f(i))
    
    print(output)

l=[1,2,3,4,5]

# transform(sqr,l) # hof
 

# Rather than making new function use lambda function 
transform(lambda x:x**2,l)
transform(lambda x:x**3,l)


# map() filter() reduce()  these 3 are HOF

# map()    → Transform / Modify data
# filter() → Select / Filter data
# reduce() → Reduce data to a single value



# Difference Between map(), filter(), and reduce()
# map()    → Modifies every element
# filter() → Keeps matching elements
# reduce() → Produces a single value

# map()    → Many outputs
# filter() → Few or many outputs
# reduce() → One output

# map()    → Transformation
# filter() → Selection
# reduce() → Aggregation/Combination