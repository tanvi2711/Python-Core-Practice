lst = [10, 20, 30, 40, 50]
element = 90

for i in lst:
    if element==i:
        print(" Element exists in the list")
        break
else:
    print(" Element does not exists in the list")


if element in lst:
    print(" Element exists in the list")
else:
    print(" Element does not exists in the list")