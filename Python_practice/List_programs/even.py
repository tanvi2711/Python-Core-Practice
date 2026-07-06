# given the list a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], you might want to extract the even numbers [2, 4, 6, 8, 10].

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


x=filter(lambda x : x%2==0,a)

print(list(x))