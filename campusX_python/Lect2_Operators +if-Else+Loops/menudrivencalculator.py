num1=int(input("Enter the 1st no: "))
num2=int(input("Enter the 2nd no: "))

op=input("Enter the operation u have to perform: ")

if op=='+':
    print(num1,"+",num2 ," : ",num1+num2)
elif op=='-':
    print(num1,"-",num2, " : ",num1-num2)
elif op=='*':
    print(num1,"*",num2 ," : ",num1*num2)
elif op=='/':
    print(num1,"/",num2 ," : ",num1/num2)
elif op=='%':
    print(num1,"%",num2, " : ",num1%num2)
else:
    print("invalid operation")
