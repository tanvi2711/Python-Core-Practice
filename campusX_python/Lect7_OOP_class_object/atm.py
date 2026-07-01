class atm():
    


    # constructor  (special function) superpower--> we dont have to call this function to exectute it will exectue by defalut after creating an object
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()


    def menu(self):
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
        self.balance=user_balance

        print("Pin created successfully!!!!!!!")
        self.menu()

    def change_pin(self):
        old_pin=input('Enter your old pin: ')

        if old_pin==self.pin:
            # let them change pin

            new_pin=input('Enter your pin: ')
            self.pin=new_pin
            print("Pin changed successfully!!!!!!!")
            self.menu()
        else:
            print("Entered pin is incorrect")
            self.menu()

    def check_balance(self):
        user_pin=input('Enter your pin: ')

        if user_pin==self.pin:
            # let them chaeck balance
            print(f'Total balance : {self.balance}')
            self.menu()
        else:
            print("Entered pin is incorrect")
            self.menu()

    def withdraw(self):
        user_pin=input('Enter your pin: ')

        if user_pin==self.pin:
            withdraw_amt=int(input("Enter Amount : "))

            if withdraw_amt <= self.balance:
                self.balance-=withdraw_amt
                print(f'Withdrawal successful Total balance : {self.balance}')
            else:
                print("Ur account does not have enough amount to withdraw")
        else:
            print("Entered pin is incorrect")
        self.menu()

myAtm=atm()
