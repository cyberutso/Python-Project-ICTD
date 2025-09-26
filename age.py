#guess my age python game 

import random as r
secret_age=r.randint(1,10)
flag=False

def game_function(guseed_age,secret):

    if(guseed_age<secret):
        return "YOU ARE TOO LOW"
    elif(guseed_age>secret):
        return "YOU ARE TOO HIGH"
    else:
        return " CORRECT"


for i in range(1,6):
    print("Take a guess,You have "+str(6-i)+" guess left.")
    guess=int(input())
    if game_function(guess,secret_age)=="CORRECT":
        print("You won the game!")
        flag=True
        break
if not flag:
    print("You lose the game !")
