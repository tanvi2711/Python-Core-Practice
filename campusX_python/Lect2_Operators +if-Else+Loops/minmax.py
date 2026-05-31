a=int(input("First num: "))
b=int(input("Second num: "))
c=int(input("Third num: "))

# Smallest no
if a<b and a<c:
    print("Smallest is :",a)
elif b<c:
    print("Smallest is :",b)
else:
    print("Smallest is :",c)