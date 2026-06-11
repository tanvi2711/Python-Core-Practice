# Creating a List

print("----------Creating a List----------")

l=[]

# Empty 
print(l)
print([])

# 1D -> Homo
print([1,2,3,4,5,6])

# Hetrogenous
print([1,'r',2,3,'t',4,(5+1j),5,6])

# 2D
print([1,2,3,[0,9],4,5,6])

# 3D
print([[[1,2],[3,4]],[[5,6],[7,8]]])

# Using Type conversion
print(list("hello"))


# Accessing Items from a List

print("----------Accessing Items from a List----------")


# indexing

print("indexing")
l=[1,2,3,4,5]
# positive
print(l[0])
print(l[-1])

l=[1,2,3,[4,5]]
print(l[-1])
print(l[-1][-1])
print(l[-1][-2])
print(l[3][0])

l=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(l[1][0][0])


#slicing
l=[1,2,3,4,5]

print("slicing")
print(l[1:5])
print(l[1:])
print(l[:-1])
print(l[-2:])

print(l[0::2])  #2 is step here
print(l[ -5:-2:2])

print("reverse")
print(l[::-1])

# ## Adding Items to a List

print("----------Adding Items to a List----------")

# append
print("append")   #append used to add one item in list
l.append(0) 
print(l)
l.append([9,0]) 
print(l)

# extend
print("extend")  #extend used to add multiple item in list
l=[1,2,3,4,5]
l.extend("hello")
l.extend(["hello"])
l.extend([9,0 ,[00,78],'tanvi',True])
print(l)


# insert
print("insert") # if i have to insert any elemnt at any position 
l=[1,2,3,4,5]
l.insert(1,60)
print(l)


# Editing items in a List

print("----------Editing items in a List----------")

k=[1,3,5,6,7]

# editing with indexing
k[3]=200
k[-3]=00
print(k)

# editing with slicing
k[1:3]=[20,30,40]
print(k)


# Deleting items from a List
print("----------Deleting items from a List----------")

l=[1,2,3,4,5,6]


# del
# del l
# indexing
del l[-1]
print(l)

del l[3]
print(l)

# slicing
del l[1:3]
print(l)


# remove
l=[1,2,3,4,5,6]
l.remove(2)    # it will delete exact no means we dont have to tell index here
l.remove(5)
print(l)

# pop
l=[1,2,3,4,5,6]
l.pop()  # it will delete last element or particular element
l.pop(0)  #index
print(l)

# clear
l=[1,2,3,4,5,6]
l.clear()
print(l)



# Operations on Lists
print("---------Operations on Lists----------")

l=[1,2,3,4]
l1=[3,4,5,6]

# Arithmetic (+,*)
print(l+l1)
print(l*3) #l*l*l

# Membership
print(5 in l)
print(5 not in l)

l2=[3,4,5,6,[7,8]]
print(7 in l2)                            

# Loop
s=[]

n=int(input("How many no u want in list:"))

for i in range(1,n+1):
    j=int(input(f"Enter {i} element: "))
    s.append(j)

print(s)


# List Functions
print("-------------List Functions--------------")

# len/min/max/sorted
l=[1,2,3,32,4,5,6]

print(len(l))
print(min(l))
print(max(l))
print(sorted(l))
print(sorted(l,reverse=True))


# count 
l=[1,2,1,4,2,1,3,4,2]
print(l.count(2))

# index
print(l.index(4))

# reverse
l=[1,4,3,32,9,4,8,6]
l.reverse() # permanently reverses the list
print(l)

# sort (vs sorted)
l=[1,4,3,32,9,4,8,6]
print(sorted(l))  #temprory operation no change in original
print(l)
l.sort() #permanent operation
print(l)

# copy -> shallow                                  
l=[1,4,4,8,6]
print(l)
print(id(l))
l1=l.copy()
print(l1)
print(id(l1))

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



print("------------traverse a list-------------")
# 2 ways to traverse a list


print("---------itemwise------------")
# itemwise
l=[1,3,4,2,4]
for i in l:
    print(i)


print("-------indexwise-----------")
# indexwise
for i in range(0,len(l)):
    print(f"{i} is index of {l[i]}")



print("---------Zip----------")
# Zip
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.


# Write a program to add items of 2 lists indexwise

L1 = [1,2,3,4]
L2 = [-1,-2,-3,-4]

print(list(zip(L1,L2)))

print([i+j for i,j in zip(L1,L2)])

print("--------charactristic of list ------------")
# List can contain any kind of objects in python
l=[1,2,print,type,input]
print(l)
# o/p=[1, 2, <built-in function print>, <class 'type'>, <built-in function input>]



# Disadvantages of Python Lists
# Slow
# Risky usage
# eats up more memory

print("-----------Risky usage------------")
a=[1,2,3]
# b=a
b=a.copy()  # if we did this it will point diff memory locations 
print(a)
print(b)

a.append(4)
print(a)
print(b)

# Becoz list are mutabble when we did a=b it will point same memory location

         