# Q8:- Given the first 2 terms of an Arithmetic Series.Find the Nth term of the series. Assume all inputs are provided by the user.

# Formula for Nth term of an Arithmetic Progression:
# Nth Term = First Term + (n - 1) * (Second Term - First Term)

a1=int(input("Enter 1st term of an Arithmetic Series : "))
a2=int(input("Enter 2nd term of an Arithmetic Series : "))
n = int(input("Enter value of n: "))

nth_term=a1+(n-1)* (a2-a1)
print("Nth term of the series: ",nth_term)