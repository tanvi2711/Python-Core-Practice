# Problem-10`:Write a python program that receives a list of strings and performs bag of word operation on those strings

# https://en.wikipedia.org/wiki/Bag-of-words_model

# i/p= 
# sentences = [
#     "hello world",
#     "hello machine learning",
#     "hello hello world"
# ]

# o/p=
# [
#  [1, 1, 0, 0],   # "hello world"
#  [1, 0, 1, 1],   # "hello machine learning"
#  [2, 1, 0, 0]    # "hello hello world"
# ]



sentences = [
    "hello world",
    "hello machine learning",
    "hello hello world"
]


def bag_of_word(s):
    l=[]
    for i in s:
        for j in i.split():
            if j not in l:
                l.append(j)

    return l

x=bag_of_word(sentences)

def seq(l,s):
    
    l2=[]
    

    for i in range(0,len(s)):
        l1=[]
        for j in l:
            k=s[i].split()
            l1.append(k.count(j))
        l2.append(l1)
    return l2


seq(x,sentences)

print(seq(x,sentences))



