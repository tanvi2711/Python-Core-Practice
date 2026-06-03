# ###`Problem 11`: A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
# The trace of robot movement is shown as the following:
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# ```
# > The numbers after the direction are steps. 

# > `!` means robot stop there.

# **Please write a program to compute the distance from current position after a sequence of movement and original point.** 

# *If the distance is a float, then just print the nearest integer.*

# Example:

# `Input`:
# ```
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# !
# ```
# `Output`:
# ```
# 2
# ```


distance=0

while True:
    x1=int(input("UP "))
    x2=int(input("DOWN  "))
    y1=int(input("LEFT  "))
    y2=int(input("RIGHT "))
    distance= ( (x2-x1)**2 + (y2-y1)**2)** 0.5  
    stop=input()
    if stop=='!':
        break
    
print(distance)