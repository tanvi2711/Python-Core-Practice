# Write OOP classes to handle the following scenarios:
# A user can create and view 2D coordinates
# A user can find out the distance between 2 coordinates
# A user can find find the distance of a coordinate from origin
# A user can check if a point lies on a given line
# A user can find the distance between a given 2D point and a given line


class point:

    def __init__(self,x,y):
        self.x_cod=x 
        self.y_cod=y

    # A user can create and view 2D coordinates
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)
    

    # A user can find out the distance between 2 coordinates
    def euclidian_distance(self,other):
        distance=((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
        return distance


    # A user can find find the distance of a coordinate from origin
    def distance_from_origin(self):
        return (self.x_cod**2+self.y_cod**2)**0.5
        # return self.euclidian_distance(point(0,0))


class line:

    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return  '{}x + {}y + {} = 0'.format(self.A,self.B,self.C)
        

    # A user can check if a point lies on a given line   
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
            return 'Lies on the line'
        else:
            return 'Does not lie on the line'


    # A user can find the distance between a given 2D point and a given line
    def shortest_distance(line,point):
        return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2+line.B**2)**0.5


p1=point(1,1)
p2=point(-1,-2)

print(p1)
print(p2)


# here p1 is 1st argument n p2 is 2nd argument
print("Distance: ",p1.euclidian_distance(p2))

print('Distance from origin: ',p1.distance_from_origin())


l=line(1,1,-2)

print(l)

print(l.point_on_line(p1))

print(l.shortest_distance(p1))