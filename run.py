import random

name = input("Hello! What is your name?: ").capitalize()
print(f"Welcome {name}, let's play!")

user_score = 0
computer_score = 0

selection = ["rock", "paper", "scissors"]

while True:
    user_input = input("Make a choice: Rock, Paper, Scissors or Q?: ").lower()
    if user_input == "q":
        print("Sorry to see you go!")
        break

    if user_input not in selection:
        print("Please make a valid selection!")
        continue
    
    random_num = random.randint(0, 2)
    # rock is 0, paper is 1 and scissors is 2
    computer_pick = selection[random_num]
    print("Computer picked", computer_pick + "!")

    if user_input == "rock" and computer_pick == "scissors":
        print("Congratulations, you win!")
        user_score += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("Congratulations, you win!")
        user_score += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("Congratulations, you win!")
        user_score += 1
    
    elif user_input == computer_pick:
        print("It's a draw!")
    
    else:
        print("Sorry, you lost!")
        computer_score += 1

print("You won", user_score, "time(s).")
print("Computer won", computer_score, "time(s).")
print("Thanks for playing!")

