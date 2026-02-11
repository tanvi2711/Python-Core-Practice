# Reverse a number (1234 → 4321)

num=int(input("Enter any no: "))
# b=1
# i=0
# while(num>0):
# 	a=num%10
# 	i=i+b*a
# 	i=a
# 	num=num//10
# 	print(b,a,num)
# 	b*=10

# print(i)
	
rev=0
while(num>0):
    rev=(rev*10)+num%10	
    num=num//10
print(rev)
