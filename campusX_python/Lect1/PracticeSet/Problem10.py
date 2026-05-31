# Q10:- Given the height, width and breadth of a milk tank, you have to find out how many glasses of milk can be obtained? Assume all the inputs are provided by the user.

# Input:
# Dimensions of the milk tank
# H = 20cm, L = 20cm, B = 20cm

# Dimensions of the glass
# h = 3cm, r = 1cm

height=int(input("Height of milk tank: "))
width=int(input("Width of milk tank: "))
breadth=int(input("Breadth of milk tank: "))

volume_of_milk_tank=height*width*breadth
print("Volume of Milk tank: ",volume_of_milk_tank)

h=int(input("Height of glass: "))
r=int(input("Radius of glass: "))

volume_of_glass=3.14*(r**2)*h
print("Volume of glass: ",volume_of_glass)

glasses_of_milk=volume_of_milk_tank//volume_of_glass
print("Total glasses of milk can be obtained: ",glasses_of_milk)