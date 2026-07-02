# ==========================================
# Static Variable (Class Variable) in Python
# ==========================================

# Definition:
# A Static Variable (Class Variable) is a variable
# that belongs to the class, not to individual objects.
# It is shared by all objects of the class.

# Syntax:
# class ClassName:
#     variable_name = value

# Why is it used?
# - To store common data shared by all objects.
# - Saves memory because only one copy is created.
# - If the value changes, it is updated for every object.

# Key Points:
# 1. Declared inside the class but outside methods.
# 2. Shared among all objects.
# 3. Access using:
#       ClassName.variable
#       object.variable
# 4. Best practice: Modify using ClassName.variable.


# Example:

# class Student:

    # Static Variable (Shared by all objects)
    # college = "ABC College"

    # def __init__(self, name):
        # Instance Variable (Different for every object)
        # self.name = name


# Creating Objects
# s1 = Student("Tanvi")
# s2 = Student("Rahul")

# Access Static Variable
# print(s1.college)
# print(s2.college)
# print(Student.college)

# Output:
# ABC College
# ABC College
# ABC College


# Changing Static Variable
# Student.college = "XYZ College"

# print(s1.college)
# print(s2.college)

# Output:
# XYZ College
# XYZ College


# ==========================================
# Static Variable vs Instance Variable
# ==========================================

# Static Variable
# ---------------
# Belongs to the class
# Shared by all objects
# Only one copy is created
# Declared inside class, outside methods

# Instance Variable
# -----------------
# Belongs to an object
# Each object has its own copy
# Created when object is created
# Declared using self inside methods


# ==========================================
# Memory Representation
# ==========================================

#               Student Class
#        -------------------------
#        college = "ABC College"
#        -------------------------
#             ↑            ↑
#             |            |
#        s1 Object     s2 Object
#        name="Tanvi"  name="Rahul"

# Both objects use the same static variable.


# ==========================================
# Interview Definition
# ==========================================

# Static Variable (Class Variable):
# A variable that belongs to the class rather than
# individual objects. It is shared among all objects,
# and only one copy exists in memory.


class atm():
    
    __counter=1

    def __init__(self):
        self.pin = ''
        self.__balance = 0 
        # self.cid=0  # it will execute for each obj n results in cid of each obj is 1
        # self.cid+=1  

        self.cid=atm.__counter
        atm.__counter=atm.__counter+1
        # self.menu()

    @staticmethod
    def get_counter():
        return atm.__counter

    def get_balance(self):
        return self.__balance


    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Only integer allow")


    def __menu(self):
        user_input = input('''
Hi how can I help you?
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Anything else to exit     
''')

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdraw()
        else:
            exit("Exit")
    
    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.pin = user_pin

        user_balance = int(input('Enter your balance: '))
        self.__balancebalance = user_balance

        print("Pin created successfully!!!!!!!")

    def change_pin(self):
        old_pin = input('Enter your old pin: ')

        if old_pin == self.pin:
            new_pin = input('Enter your pin: ')
            self.pin = new_pin
            print("Pin changed successfully!!!!!!!")
        else:
            print("Entered pin is incorrect")

    def check_balance(self):
        user_pin = input('Enter your pin: ')

        if user_pin == self.pin:
            print(f'Total balance : {self.balance}')
        else:
            print("Entered pin is incorrect")

    def withdraw(self):
        user_pin = input('Enter your pin: ')

        if user_pin == self.pin:
            withdraw_amt = int(input("Enter Amount : "))

            if withdraw_amt <= self.__balance:
                self.__balance -= withdraw_amt
                print(f'Withdrawal successful Total balance : {self.__balance}')
            else:
                print("Ur account does not have enough amount to withdraw")
        else:
            print("Entered pin is incorrect")


# to avoid this will convert counter into private variable
# atm.counter='hehhe'


c1 = atm() 
c2 = atm()
c3 = atm()

# print(c1.get_counter())
print(atm.get_counter())



print(c1.cid)
print(c2.cid)
print(c3.cid)

