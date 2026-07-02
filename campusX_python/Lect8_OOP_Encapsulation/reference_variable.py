# Reference Variables
# Reference variables hold the objects
# We can create objects without reference variable as well
# An object can have multiple reference variables
# Assigning a new reference variable to an existing object does not create a new object

# object without a reference
class Person:

  def __init__(self):
    self.name = 'nitish'
    self.gender = 'male'


Person()
print(Person())


p = Person()
q = p

# Multiple ref
print(id(p))
print(id(q))

# change attribute value with the help of 2nd object
print(p.name)
print(q.name)
q.name='tanvi'
print(q.name)
print(p.name)
