import random
secret=random.randint(1,10)
temp=input("guess a number\n")
guess=int(temp)
time=1
while (guess!=secret)and(time<3):
    if guess>secret:
        print("bit large")
    else:
        print("bit small")
        
    temp=input("try again\n")
    guess=int(temp)
    time+=1
if(time<=3)and(guess==secret):
    print("true")
else:
     print("times up")
     


       
