class atm():
    
    def __init__(self):
        self.pin = ''
        self.__balance = 0      # Private variable (cannot be accessed directly from outside)
        # self.menu()

    # ==========================
    # Getter Method
    # ==========================
    # Used to READ/ACCESS the value of a private variable.
    # Why?
    # - Since __balance is private, it cannot be accessed directly.
    # - Getter provides controlled access to the private data.
    # - This is a part of Encapsulation (data hiding).
    def get_balance(self):
        return self.__balance

    # ==========================
    # Setter Method
    # ==========================
    # Used to UPDATE/MODIFY the value of a private variable.
    # Why?
    # - It allows validation before changing the data.
    # - Here, only integer values are accepted.
    # - Prevents invalid data from being stored.
    # - This protects the object and maintains data integrity.
    # - This is also a part of Encapsulation.
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


myAtm = atm()

print(myAtm.get_balance())

myAtm.set_balance(1000)

print(myAtm.get_balance())

myAtm.set_balance('hehehe')

print(myAtm.get_balance())

myAtm.withdraw()

# Encapsulation:
# Hiding data using private variables (__variable)
# and providing controlled access through Getter and Setter methods.



# Short Note (for your notebook):

# Getter: Used to access (read) a private variable.
# Setter: Used to modify (update) a private variable after validating the input.
# Why use them? They protect the data, prevent invalid values, and provide controlled access to private variables.
# Encapsulation = Data Hiding + Controlled Access (using Private variables, Getters & Setters).

