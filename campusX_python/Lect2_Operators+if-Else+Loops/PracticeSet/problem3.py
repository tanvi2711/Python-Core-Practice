# Problem 3: Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit.


sp=int(input("Enter Selling Price: "))
cp=int(input("Enter Cost Price: "))


if sp>cp:
    print("Profit : Rs.",sp-cp)
elif sp<cp:
    print("Loss : Rs.",cp-sp)
else:
    print("Break-even : Rs.",sp-cp)