# parent
class user:

    def __init__(self):
        self.name='Tanvi'
        self.gender='Female'

    def login(self):
        return 'login'


# child
class student(user):    #inherite the parent class 

    # def __init__(self):     #here method overidding is happen due to this its not working
    #     self.roll_no=100

    def enroll(self):
        return "Eroll into the class"


u=user()
s=student()

print(s.name)
print(s.gender)
# print(s.roll_no)
print(s.login())
print(s.enroll())



