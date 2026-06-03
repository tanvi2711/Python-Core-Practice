import random

jackpot=random.randint(1,100)

num=int(input("Guess no btw 1 to 100 : "))

count=1
while num!=jackpot:
    if num<jackpot:
        print("Wrong! Guess higher")
    else:
        print("Wrong! guess lower")
    
    num=int(input("Guess no btw 1 to 100 : "))
    count+=1

else:
    print("Correct guess")
    print("Attempts: ",count)
    