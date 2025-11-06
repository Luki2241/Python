import random

choicebot = ""
choice = ""
wins = 0
losses = 0
print("Welcome to rock, paper, scissors!")
# main loop
while True:
    choice = input("Enter your move: ").lower()
    print("You have chosen:", choice)
    choicebot = random.choice(["rock", "paper", "scissors"])
    print("The bot has chosen:", choicebot)
    # main game
    if choice == "rock" and choicebot == "rock":
        print("It's a tie!")
    elif choice == "rock" and choicebot == "paper":
        print("1 point for the bot!")
        losses += 1
    elif choice == "rock" and choicebot == "scissors":
        print("1 point for you!")
        wins +=1
    elif choice == "paper" and choicebot == "paper":
        print("It's a tie!")
    elif choice == "paper" and choicebot == "rock":
        print("1 point for you!")
        wins +=1
    elif choice == "paper" and choicebot == "scissors":
        print("1 point for the bot!")
        losses += 1
    elif choice == "scissors" and choicebot == "scissors":
        print("It's a tie!")
    elif choice == "scissors" and choicebot == "paper":
        print("1 point for you!")
        wins +=1
    elif choice == "scissors" and choicebot == "rock":
        print("1 point for the bot!")
        losses += 1
    else:
        print("Invalid choice.")
    # checks win and losses
    if wins == 3:
        print("You win!")
        quit()
    if losses == 3:
        print("You lose!")
        quit()