# Problem 4: Write a menu-driven program -
# cm to ft
# km to miles
# USD to INR
# exit

measure=input("""
1.Enter 1 for cm to ft
2.Enter 2 for km to miles
3.Enter 3 for USD to INR
4.Enter 4 exit 
""")


if measure == '1':
    cm=float(input("Enter cm: "))
    ft=cm*0.0328084
    print("Feet: ",ft)
elif measure == '2':
    km=float(input("Enter km: "))
    miles=km*0.621371
    print("Miles: ",miles)
elif measure == '3':
    usd=float(input("Enter USD: "))
    inr=usd*95.59
    print("INR: ",inr)
else:
    exit
