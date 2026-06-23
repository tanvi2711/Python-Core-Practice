# Q1:` Join Tuples if similar initial element
# While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

# For eg.
# Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 

l=[]
t=[]
print(test_list[3][1])


for i in range(len(test_list)):
    for j in test_list:
        print(test_list[i])





    # for j in range(1):
    #     print(i[j],(i)[j])
    #     if i[j]==i[j+1]:
    #         l.append(j)
           
    # t.append(tuple(l))



        


# for i,j in test_list:
#     for k in range(len(test_list)):
#         print(test_list[k])
#         if i not in l:
#             l.append(j)
    
#     # t.append()

print(t)


