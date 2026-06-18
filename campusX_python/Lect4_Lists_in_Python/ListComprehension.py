# List Comprehension
print("-------------List Comprehension--------------")

# List Comprehension provides a concise way of creating lists.

# its a shortcut to create list

# newlist = [expression for item in iterable if condition == True]


# Advantages of List Comprehension

# More time-efficient and space-efficient than loops.
# Require fewer lines of code.
# Transforms iterative statement into a formula.


# Add 1 to 10 numbers to a list
l=[]


# TRADITIONAL APPROCH
# for i in range(1,12):
#     l.append(i)

# print(l)

l=[i for i in range(1,12)]
print(l)


# scalar multiplication on a vector
v=[1,2,3]
s=-3

v=[s*i for i in v ]
print(v)

# Add square
s=[3,2,4]

s=[i**2 for i in s]
print(s)

# Print all numbers divisible by 5 in the range of 1 to 50
d=[]

d=[i for i in range(1,51) if i%5==0 ]
print(d)

# find languages which start with letter p
languages = ['java','python','php','c','javascript']

languages=[language for language in languages if language.startswith('p')]
print(languages)



# Nested if with List Comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

# add new list from my_fruits and items if the fruit exists in basket and also starts with 'a'

new=[]
new=[item for item in my_fruits if item in basket if item.startswith('a')]
print(new)


# Print a (3,3) matrix using list comprehension -> Nested List comprehension
print([[i*j for i in range(1,4)] for j in range(1,4)])  # 1st outer loop then inner loop



# Traditional
# l=[]

# for i in range (1,4):
#     r=[]
#     for j in range(1,4):
#         r.append(i*j)
#     l.append(r)
# print(l)

# cartesian products -> List comprehension on 2 lists together
l1=[1,2,3,4]
l2=[5,6,7,8]

print([i*j for i in l1 for j in l2])