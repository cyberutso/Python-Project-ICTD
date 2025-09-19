import random
item_list=["Rock","Paper","Scissors"]
user_choice=input("Enter your move:Rock, Paper, Scissor = ")
computer_choice=random.choice(item_list)
print(f"User Choice = {user_choice},computer Choice = {computer_choice}")
#condition
if user_choice==computer_choice:
    print("Match Tie") 
#condition for Rock    
elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Computer win")
    else:
        print("You Win")
#condition for paper
elif user_choice=="Paper":
    if computer_choice=="Scissor":
        print("Computer win")
    else:
        print("You Win")
#Condition for Scissor
elif user_choice=="Scissor":
    if computer_choice=="Paper":
        print("You win")
    else:
        print("Computer Win")         