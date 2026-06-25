# Problem 15- A dictionary contains following information about 5 employees:
# - First name
# - Last name
# - Age
# - Grade(Skilled,Semi-skilled,Highly skilled)<br>
# Write a program using map/filter/reduce to a list of employees(first name + last name) who are highly skilled

import functools

employees = [
    {
        'fname':'Nitish',
        'lname':'Singh',
        'age' : 33,
        'grade':'skilled'
    },
    {
        'fname':'Ankit',
        'lname':'Verma',
        'age' : 34,
        'grade':'semi-skilled'
    },
    {
        'fname':'Neha',
        'lname':'Singh',
        'age' : 35,
        'grade':'highly-skilled'
    },
    {
        'fname':'Anurag',
        'lname':'Kumar',
        'age' : 30,
        'grade':'skilled'
    },
    {
        'fname':'Abhinav',
        'lname':'Sharma',
        'age' : 37,
        'grade':'highly-skilled'
    }
]



hskill_emp=list(filter(lambda x: x['grade']=='highly-skilled',employees))

print(hskill_emp)

fl_name=list(map(lambda x: x['fname']+" "+x['lname'],hskill_emp))

print(fl_name)