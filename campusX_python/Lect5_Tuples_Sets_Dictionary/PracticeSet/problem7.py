# Q2: Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.

# Input:`
# Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

# Output:`
# No of unique vowels-6

st = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

s=st.split()

vowels=['a','e','i','o','u','A','E','I','O','U']

u=set()


for i in s:
    for j in vowels:
        if j in i:
            u.add(j)
print(f"No of unique vowels- {len(u)}")