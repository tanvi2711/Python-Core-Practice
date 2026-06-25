# Problem-2:Write a Python function that accepts a hyphen-separated sequence of words as parameter and returns the words in a hyphen-separated sequence after sorting them alphabetically.

# Input:
# green-red-yellow-black-white

# Output:
# black-green-red-white-yellow


def str_sort(s):
    if '-' in s:
        s=s.split('-')
        n=''
        d=''
        for i in sorted(s):
            n=n+d+i
            d='-'
        return n



print(str_sort("green-red-yellow-black-white"))


