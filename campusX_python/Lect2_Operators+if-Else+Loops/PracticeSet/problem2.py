# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


ang1=int(input("Enter angle: "))
ang2=int(input("Enter angle: "))
ang3=int(input("Enter angle: "))


if (ang1+ang2+ang3)==180:
    print("It can form a triangle")
else:
    print("It can not form a triangle")