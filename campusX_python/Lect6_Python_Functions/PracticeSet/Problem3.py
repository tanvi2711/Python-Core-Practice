# Problem 3:Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# Sample String : 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'
# Expected Output :
# No. of Upper case characters :  9
# No. of Lower case Characters :  47

def count_char(s,cu,cl):
    for i in s:
        if i >='A' and i<='Z':
            cu+=1
        if i >='a' and i<='z':
            cl+=1  
    return f'No. of Upper case characters : {cu} \nNo. of Upper case characters : {cl}'
    
    
s='CampusX is an Online Mentorship Program fOr EnginEering studentS.'
print(count_char(s,0,0))
