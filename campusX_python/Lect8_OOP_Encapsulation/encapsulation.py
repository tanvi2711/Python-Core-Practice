class atm():
    
    def __init__(self):
        self.pin=''
        self.__balance=0    # it become private variable
        # self.menu()


    def __menu(self):
        user_input = input('''
Hi how can I help you?
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Anything else to exit     
''')

        if user_input=='1':
            # create pin
            self.create_pin()
        elif user_input=='2':
            # change pin
            self.change_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw()
        else:
            exit("Exit")
    
    def create_pin(self):
        user_pin=input('Enter your pin: ')
        self.pin=user_pin

        user_balance=int(input('Enter your balance: '))
        self.__balancebalance=user_balance

        print("Pin created successfully!!!!!!!")

    def change_pin(self):
        old_pin=input('Enter your old pin: ')

        if old_pin==self.pin:
            new_pin=input('Enter your pin: ')
            self.pin=new_pin
            print("Pin changed successfully!!!!!!!")
        else:
            print("Entered pin is incorrect")

    def check_balance(self):
        user_pin=input('Enter your pin: ')

        if user_pin==self.pin:
            # let them chaeck balance
            print(f'Total balance : {self.balance}')
        else:
            print("Entered pin is incorrect")

    def withdraw(self):
        user_pin=input('Enter your pin: ')

        if user_pin==self.pin:
            withdraw_amt=int(input("Enter Amount : "))

            if withdraw_amt <= self.__balance:
                self.__balance-=withdraw_amt
                print(f'Withdrawal successful Total balance : {self.__balance}')
            else:
                print("Ur account does not have enough amount to withdraw")
        else:
            print("Entered pin is incorrect")


myAtm=atm()


myAtm.create_pin()
myAtm.__balance='heehhe' 
# myAtm._atm__balance='heehhe'    # user can change value like this from outside of class 

myAtm._atm__balance=10999    

myAtm.withdraw()

print(myAtm._atm__balance)
print(myAtm.__balance)

# output:-
# 0
# heehhe


# here while withdraw function exection error raise but in this code anyone can change the data of variables from outside 
# so here we can change our atributes to private which will prevent accessing data from outside of code


# private variable = __   


# in java private means it become private we cant access it outside of code
# but in python nothing is truely private programmer can change it by using '_atm__balance ' format 

# becoz python is made for adults  



# after we made a private variable or anything it become seprate variable '_atm__balance ' in this format it no more __balance or balance 