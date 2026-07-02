# instance var
class Person:

  def __init__(self,name_input,country_input):
    self.name = name_input
    self.country = country_input

p1 = Person('nitish','india')
p2 = Person('steve','australia')

print(p1.name)

# here name n country are instance variable means class variable

# for every object value is different 
# for ex above for p1 we have 2 diff values n p1 have 2 diff values
