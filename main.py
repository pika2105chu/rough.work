import random

#  snake = 1, water = 0, gun = 2

youdict = {0:'Water' , 1:'Snake' , 2:'Gun'}
computer = random.choice([0,1,2])
you = int(input("Enter your choice : "))

print(f"computer input : {youdict[computer]}")
print(f"your input : {youdict[you]}")

if(you not in (0,1,2)):
    print("You are giving invalid input, enter between 0,1,2 ")
    
if(you == computer):
    print("Your inputs are same, so its DRAW !!")
else:
    if(computer==0 and you==1):               #-1 win
        print("You Win!")
    elif(computer==0 and you==2):   #-2 lose
        print("You Lose!")
    elif(computer==1 and you==0):   #1 lose
        print("You Lose!")
    elif(computer==1 and you==2):            #-1 win
        print("You Win!")
    elif(computer==2 and you==0):            #2 win
        print("You Win!")
    elif(computer==2 and you==1):   #1 lose
        print("You Lose!")

