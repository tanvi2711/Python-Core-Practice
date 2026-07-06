num=int(input("Enter any no: "))

n=num
arm=0

while num!=0:
    r=num%10
    arm+=r**3
    num=num//10
    if n==arm:
        print(f'{arm} is armstrong number')

if arm!=n:
    print(f'{n} is not armstrong number')

