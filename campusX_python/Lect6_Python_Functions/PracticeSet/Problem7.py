# Problem-7 Write a python function that accepts a string as input and returns the word with most occurence.

# Input:
# hello how are you i am fine thank you

# Output
# you -> 2


def word_occ(s):
    l=s.split()
    d={}
    for i in l:
        d[i]=l.count(i)
    x=max(d.values())
    for j,k in d.items():
        if x==k:
            print(f'{j}-->{x}')

st='hello how are you i am fine thank you fine fine fine'

word_occ(st)