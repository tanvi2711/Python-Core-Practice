# ==========================================
# Method Overriding in Python
# ==========================================

# Definition:
# Method Overriding occurs when a Child class
# redefines a method that already exists
# in the Parent class.

# Important Points:
# ✔ Parent and Child method names must be the same.
# ✔ Child method is executed instead of Parent method.
# ✔ Represents Runtime Polymorphism.


# ==========================================
# Parent Class
# ==========================================

class Phone:

    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")

        self.__price = price      # Private Attribute
        self.brand = brand        # Public Attribute
        self.camera = camera      # Public Attribute

    def buy(self):
        print("Buying a Phone")

    # Getter to access private attribute
    def get_price(self):
        return self.__price


# ==========================================
# Child Class
# ==========================================

class SmartPhone(Phone):

    # Overriding Parent's buy() method
    def buy(self):
        print("Buying a SmartPhone")


# Creating Child Object
s = SmartPhone(20000, "Apple", 13)

# Calls Child's overridden method
s.buy()

# Parent's public attributes
print("\nBrand  :", s.brand)
print("Camera :", s.camera)

# Accessing Parent's private attribute using Getter
print("Price  :", s.get_price())


# ==========================================
# Interview Points
# ==========================================

# ✔ Child method overrides Parent method.
# ✔ Method name should be the same.
# ✔ Parent constructor is inherited and executes automatically.
# ✔ Private attributes are accessed using Getter methods.
# ✔ Method Resolution Order (MRO):
#   Child Class → Parent Class → object