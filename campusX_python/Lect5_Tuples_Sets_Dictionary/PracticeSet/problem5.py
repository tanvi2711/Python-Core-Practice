# Q5`: Shortlist Students for a Job role
# Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

# Show every students record in form of tuples if matches all required criteria.

# It is assumed that there will be only one primry skill.

# If no such candidate found, print `No such candidate`

# `Input:
# Enter No of records- 2
# Enter Details of student-1
# Enter Student name- Manohar
# Enter Higher Education- B.Tech
# Enter Primary Skill- Python
# Enter Year of Graduation- 2022
# Enter Details of student-2
# Enter Student name- Ponian
# Enter Higher Education- B.Sc.
# Enter Primary Skill- C++
# Enter Year of Graduation- 2020

# Enter Job Role Requirement
# Enter Skill- Python
# Enter Higher Education- B.Tech
# Enter Year of Graduation- 2022

# `Output
# ('Manohar', 'B.tech', 'Python', '2022')



student=[]


n=int(input("Enter No of records- "))
for i in range(n):
    print(f"Enter No of records- {i+1}")
    name=input("Enter Student name-")
    education=input("Enter Higher Education-")
    skill=input("Enter Primary Skill- ")
    year=input("Enter Year of Graduation- ")
    student.append((name,education,skill,year))


skill_req=[]

print("Enter Job Role Requirement")
skill=input("Enter Skill-")
education=input("Enter Higher Education- ")
year=input("Enter Year of Graduation- ")

count=0 

for i in student:
    if i[2]==skill and i[1]==education and i[3]==year :
        count+=1
        skill_req.append(i)

if count==0:
    print("No such candidate ")
else:    
    print(skill_req)
