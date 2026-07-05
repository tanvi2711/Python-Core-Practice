class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor {{Parent class}}")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone  {{Parent class}} ")

class SmartPhone(Phone):

    def __init__(self, price, brand, camera,os,ram):
        print ("Inside Smartphone constructor {{child class}}")
        self.os=os
        self.ram=ram
        super().__init__(price, brand, camera)
        print ("Inside Smartphone constructor {{child class}}")


    # Overriding Parent's buy() method
    def buy(self):
        print("Buying a SmartPhone {{Child class}}")

        # Calls Parent class buy() method
        # using the super() keyword.
        super().buy()
        # print(super().brand)   # we cant accessvariable using super keyword super can only access methodss

s=SmartPhone(20000, "Apple", 13,"Samsung",12)

s.buy()


# this will not work we cant use super outside the class in child class 
# s.super().buy()