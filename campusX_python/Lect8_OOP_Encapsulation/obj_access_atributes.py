# how to access attributes


class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

  def greet(self):
    if self.country == 'india':
      print('Namaste',self.name)
    else:
      print('Hello',self.name)


p = Person('nitish','india')

print(p.country)
print(p.name)
print(p.greet())

p.gender = 'Male'

print(p.gender)