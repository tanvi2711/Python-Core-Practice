# Q9:- Given 2 fractions, find the sum of those 2 fractions.Take the numerator and denominator values of the fractions from the user.

n1 = int(input("Enter value of numerator of 1st fraction: "))
d1 = int(input("Enter value of denominator of 1st fraction: "))
n2 = int(input("Enter value of numerator of 2nd fraction: "))
d2 = int(input("Enter value of denominator of 2nd fraction: "))

sum_of_fraction = ((n1*d2)+(n2*d1))/(d1*d2)

print("Sum of ",n1,"/",d1, " and" , n2,"/",d2 ,"is: ",sum_of_fraction)