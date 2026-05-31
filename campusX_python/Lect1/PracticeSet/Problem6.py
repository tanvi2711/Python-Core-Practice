# Q6:- Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

# For example: Input: heads -> 4 legs -> 12
# Output: dogs -> 2 chicken -> 2


head=int(input("Heads: "))
leg=int(input("Legs: "))

dogs=int(head/2+leg/4)
chicken=int(head/2)

print("dogs ->",dogs ,"chicken ->",chicken)