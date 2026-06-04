# Problem 19: Word location in String.
# Statement: Find a location of a word in a given sentence.

# Example 1:

# Input:

# Sentence: We can learn data science through campusx mentorship program.

# word: campusx
# Output:

# Location of the word is 7.
# Note- Don't use index/find functions

str=input("Enter any string: ")
word=input("Enter any word present in string: ")

s=str.split()


loc=0

for i in range(0,len(s)):
    if s[i]==word:
        loc=i+1
        break

print(f"Location of the {word} is {loc}")