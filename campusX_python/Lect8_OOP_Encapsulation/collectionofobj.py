# list of objects
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

# L = [p1,p2,p3]

# for i in L:
#   print(i.name,i.gender)



# d={p1:Person('nitish','male'),p2:Person('ankit','male'),p3:Person('ankita','female')}

# for i in d.values():
#   print(i.name,i.gender)


d = {'p1':p1,'p2':p2,'p3':p3}

for i in d:
  print(d[i].name,d[i].gender)