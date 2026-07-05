# ==========================================
# Private Members & Inheritance
# ==========================================

# Important Points:
# ✔ Child class cannot access Parent's private members directly.
# ✔ Use Getter methods to access private data.
# ✔ If Child has its own constructor, Parent's constructor
#   is NOT called automatically.
# ✔ Use super().__init__() to call the Parent constructor.


# ------------------------------------------
# Example 1:
# Child cannot access Parent's private members
# ------------------------------------------

# class Phone:
#
#     def __init__(self, price, brand, camera):
#         self.__price = price      # Private Variable
#         self.brand = brand        # Public Variable
#
#     def __show(self):
#         return self.__price       # Private Method
#
#
# class SmartPhone(Phone):
#
#     def check(self):
#         return self.__price       # ❌ Error (Private variable not accessible)
#
#
# s = SmartPhone(20000, "Apple", 13)
#
# print(s.brand)       # ✔ Public variable
# print(s.__show())    # ❌ Private method
# print(s.__price)     # ❌ Private variable
# print(s.check())     # ❌ Child can't access private variable


# ------------------------------------------
# Example 2:
# Accessing Private Variable using Getter
# ------------------------------------------

# class Parent:
#
#     def __init__(self, num):
#         self.__num = num          # Private Variable
#
#     def get_num(self):
#         return self.__num         # Getter
#
#
# class Child(Parent):
#
#     def show(self):
#         print("Child Class")
#
#
# son = Child(100)
#
# print(son.get_num())   # ✔ Access private data using Getter
# son.show()


# ------------------------------------------
# Example 3:
# Child Constructor Overrides Parent Constructor
# ------------------------------------------

# class Parent:
#
#     def __init__(self, num):
#         self.__num = num
#
#     def get_num(self):
#         return self.__num
#
#
# class Child(Parent):
#
#     def __init__(self, val, num):
#         self.__val = val
#         # Parent constructor is NOT called.
#
#     def get_val(self):
#         return self.__val
#
#
# son = Child(100, 10)
#
# print(son.get_num())   # ❌ Error (__num not initialized)
# print(son.get_val())   # ✔ Works


# ------------------------------------------
# Example 4:
# Child Accessing Parent's Public Members
# ------------------------------------------

class A:

    def __init__(self):
        self.var1 = 100        # Public Variable

    def display1(self, var1):
        # self.var1 refers to the instance variable (100)
        print("Class A :", self.var1)


class B(A):
    # B inherits all public members of A

    def display2(self, var1):
        # Child can directly access Parent's public variable
        print("Class B :", self.var1)


obj = B()

# Parent constructor is called automatically
# because Child has no constructor.
obj.display1(200)

# obj.display2(500)


# ==========================================
# Interview Points
# ==========================================

# ✔ Private members cannot be accessed directly by Child.
# ✔ Getter methods provide controlled access to private data.
# ✔ If Child has no constructor, Parent constructor is called automatically.
# ✔ If Child has its own constructor, use super().__init__()
#   to initialize Parent members.
# ✔ Child class can directly access Parent's public members.