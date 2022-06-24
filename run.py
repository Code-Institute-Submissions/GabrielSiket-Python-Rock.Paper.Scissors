import random

user_score = 0
computer_score = 0

selection = ["rock", "paper", "scissors"]

while True:
    user_input = input("Make a choice: Rock, Paper, Scissors or Quit?: ").lower()
    if user_input == "quit":
        print("Sorry to see you go!")
        quit()

    if user_input not in selection:
        print("Please make a valid selection!")
        continue
    
    random_num = random.randint(0, 2)
    # rock is 0, paper is 1 and scissors is 2
    computer_pick = selection[random_num]
    print("Computer picked", computer_pick + "!")


print("Thanks for playing!")

