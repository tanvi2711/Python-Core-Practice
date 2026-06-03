lower_range=int(input("Enter any no: "))
higher_range=int(input("Enter any no: "))

for i in range(lower_range,higher_range+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print("prime : ",i)


print("-----------continue-----------------")
for i  in range(1,10):
    if i==5:
        continue 
    print(i)