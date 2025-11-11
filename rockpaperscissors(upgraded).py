import random

choiceplayer = ""
choicebot = ""
choices = ["rock", "paper", "scissors"] 
#wins, ties, losses
score_tracker = [0, 0, 0]
print("Welcome to rock, paper, scissors!")
# main loop
while True:
    choiceplayer = input("Enter your move: ").lower()
    print("You have chosen:", choiceplayer)
    choicebot = random.choice(choices)
    print("The bot has chosen:", choicebot)
    # main game
    if choiceplayer == choices[0] and choicebot == choices[0]:
        print("It's a tie!")
        score_tracker[1] += 1
    elif choiceplayer == choices[0] and choicebot == choices[1]:
        print("1 point for the bot!")
        score_tracker[2] += 1
    elif choiceplayer == choices[0] and choicebot == choices[2]:
        print("1 point for you!")
        score_tracker[0] += 1
    elif choiceplayer == choices[1] and choicebot == choices[1]:
        print("It's a tie!")
        score_tracker[1] += 1
    elif choiceplayer == choices[1] and choicebot == choices[0]:
        print("1 point for you!")
        score_tracker[0] += 1
    elif choiceplayer == choices[1] and choicebot == choices[2]:
        print("1 point for the bot!")
        score_tracker[2] += 1
    elif choiceplayer == choices[2] and choicebot == choices[2]:
        print("It's a tie!")
        score_tracker[1] += 1
    elif choiceplayer == choices[2] and choicebot == choices[1]:
        print("1 point for you!")
        score_tracker[0] += 1
    elif choiceplayer == choices[2] and choicebot == choices[0]:
        print("1 point for the bot!")
        score_tracker[2] += 1
    else:
        print("Invalid choice.")
    # checks win and losses
    print("Wins:", score_tracker[0])
    print("Ties:", score_tracker[1])
    print("Losses:", score_tracker[2])
    if score_tracker[0] == 5:
        print("You win!")
        quit()
    if score_tracker[2] == 5:
        print("You lose!")
        quit()