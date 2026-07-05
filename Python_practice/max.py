a=int(input("1st number: "))
b=int(input("2nd number: "))

print("Greater: ",max(a,b))

if a>b:
    print(f"{a} is greter")
elif b>a:
    print(f"{b} is greter")
else:
    print(f"{a} is equals to {b}")

print(a if a>b else b)