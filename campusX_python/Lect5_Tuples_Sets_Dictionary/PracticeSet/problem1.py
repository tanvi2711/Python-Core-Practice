# # Q1:` Join Tuples if similar initial element
# # While working with Python tuples, we can have a problem in which we need to perform concatenation of records from the similarity of initial element. This problem can have applications in data domains such as Data Science.

# # For eg.
# # Input  : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 
# # Output : [(5, 6, 7, 8), (6, 10), (7, 13)] 


test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)] 

l=[]
t=[]

j=1
l.append(test_list[0][0])

for i in test_list:
    if j==len(test_list):
        break    
    if i[0]==test_list[j][0]:
        print(test_list[j][0],test_list[j][1])

        l.append(i[1])
    else:
        t.append(i)
        p
        print("else",test_list[j][0],test_list[j][1])

    print("j",j)
    j+=1

t.append(tuple(l))


#     # for j in range(1):
#     #     print(i[j],(i)[j])
#     #     if i[j]==i[j+1]:
#     #         l.append(j)
           
#     # t.append(tuple(l))



        


# # for i,j in test_list:
# #     for k in range(len(test_list)):
# #         print(test_list[k])
# #         if i not in l:
# #             l.append(j)
    
# #     # t.append()

print(t)


