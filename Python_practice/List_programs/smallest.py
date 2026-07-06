a = [8, 3, 5, 1,0, 9, 12]

small=a[0]
for i in a:
    if small>i:
        small=i
        continue

print("Smallest: ",small)