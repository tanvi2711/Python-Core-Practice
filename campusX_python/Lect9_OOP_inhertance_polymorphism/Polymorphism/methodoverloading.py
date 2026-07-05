# class shape:

#     def area(self,radius):
#         return 3.14* radius* radius
    
#     def area(self,l,b):
#         return l*b
    
# a=shape()

# print(a.area(3))
# print(a.area(2,4))

# Python doesn't work because Python does not support method overloading like Java or C++.
# When you define two methods with the same name, the second definition replaces the first one

# Python treats it like this:

# class shape:

#     # This method is discarded
#     def area(self, radius):
#         return 3.14 * radius * radius

#     # Only this method remains
#     def area(self, l, b):
        # return l * b




class Shape:

  def area(self,a,b=0):
    if b == 0:
      return 3.14*a*a
    else:
      return a*b

s = Shape()

print(s.area(2))
print(s.area(3,4))



class Parent:
    def display(self):
        print("Parent")

class Child(Parent):
    def display(self):
        super().display()
        print("Child")


son=Child()

print(son.display())