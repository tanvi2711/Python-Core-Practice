# ==========================================
# super() Keyword in Python
# ==========================================

# Definition:
# super() is a built-in function used to refer
# to the Parent (Super) class.

# Why use super()?
# ✔ To call Parent class methods.
# ✔ To call Parent class constructor (__init__()).
# ✔ Avoids rewriting Parent class code.
# ✔ Supports code reusability.

# Syntax:
# super().method_name()
# super().__init__(arguments)

# Example:
# super().buy()            # Calls Parent's buy() method
# super().__init__(...)    # Calls Parent's constructor


# ✔ super() refers to the Parent (Super) class.
# ✔ Used to call Parent methods and constructors.
# ✔ Commonly used in Inheritance and Method Overriding.
# ✔ Helps avoid code duplication (DRY Principle).

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):

    # Overriding Parent's buy() method
    def buy(self):
        print("Buying a SmartPhone")

        # Calls Parent class buy() method
        # using the super() keyword.
        super().buy()

s=SmartPhone(20000, "Apple", 13)

s.buy()


# if we didnt use super then parent class buy method will not call 