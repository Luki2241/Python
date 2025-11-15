import random

# declares variables
choicetool = [1, 2, 3, 4, 5, 6, 7, 8, 9]
choicetooluser = 0
kmh = 0
mph = 0
c = 0
f = 0
tasks = []
ops = ["+", "-", "/", "*"]
choicesrps = ["rock", "paper", "scissors"]
score_tracker = [0, 0, 0]
choicestask = [1, 2, 3]

# defines functions
def add(num1, num2):
    result = num1 + num2
    print(num1, "+", num2, "=", result)

def sub(num1, num2):
    result = num1 - num2
    print(num1, "-", num2, "=", result)

def div(num1, num2):
    if num2 == 0:
        print("Invalid operation.")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)

def mul(num1, num2):
    result = num1 * num2
    print(num1, "*", num2, "=", result)

def convspeed(kmh):
    kmh = int(input("Enter speed in km/h: "))
    mph = kmh / 1.609344
    print("The speed in mph is:", mph)

def convtemp(c):
    c = int(input("Enter temperature in C°: "))
    f = c * 1.8 + 32
    print("The temperature in F° is:", f)

def passchecker(password):
    password = input("Enter your password: ")

    # FIXED: previously incorrect logic
    if len(password) >= 8 and any(ch.isupper() for ch in password) and any(ch.isdigit() for ch in password):
        print("Your password is strong!")
    else:
        print("Your password is too weak!")
        print("Try adding uppercase letters and numbers.")

def taskadd():
    task = input("Enter your task name: ")
    tasks.append(task)
    print("Task added!")

def taskremove():
    if len(tasks) == 0:
        print("No tasks to remove.")
    else:
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])
        remove = int(input("Which task do you want to remove?: "))
        tasks.pop(remove - 1)
        print("Task removed!")

def taskview():
    if len(tasks) > 0:
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])
    else:
        print("There are no tasks right now.")

def palchecker():
    word = input("Enter a word: ").lower()
    reversedword = word[::-1]
    print("Reversed word:", reversedword)
    if reversedword == word:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

def randomnumgame():
    number = random.randint(1, 10)
    for i in range(3):
        gnumber = int(input("Input a number to guess: "))
        if gnumber == number:
            print("Correct!")
            return
        else:
            print("Wrong number, try again.")
    print("You lost! The number was:", number)

def rps():
    print("Welcome to rock, paper, scissors!")

    while score_tracker[0] < 5 and score_tracker[2] < 5:
        choiceplayerrps = input("Enter your move (rock/paper/scissors): ").lower()

        if choiceplayerrps not in choicesrps:
            print("Invalid choice.")
            continue

        print("You have chosen:", choiceplayerrps)
        choicebotrps = random.choice(choicesrps)
        print("The bot has chosen:", choicebotrps)

        if choiceplayerrps == choicebotrps:
            print("It's a tie!")
            score_tracker[1] += 1

        elif (choiceplayerrps == "rock" and choicebotrps == "scissors") or \
             (choiceplayerrps == "paper" and choicebotrps == "rock") or \
             (choiceplayerrps == "scissors" and choicebotrps == "paper"):
            print("1 point for you!")
            score_tracker[0] += 1
        else:
            print("1 point for the bot!")
            score_tracker[2] += 1

        print("Wins:", score_tracker[0])
        print("Ties:", score_tracker[1])
        print("Losses:", score_tracker[2])

    if score_tracker[0] == 5:
        print("You win!")
    else:
        print("You lose!")

# prints welcome        
print("Welcome to Luki's Multitool!")

# main program
while True:
    print("\n1. Calculator")
    print("2. Temperature converter (C° > F°)") 
    print("3. Speed converter (km/h to mph)")
    print("4. Password strength checker")
    print("5. To-do list tool")
    print("6. Palindrome checker")
    print("7. Number guessing game")
    print("8. Rock-paper-scissors")
    print("9. Exit")                      

    choicetooluser = int(input("Which tool or game do you want to use/play?: "))

    if choicetooluser == choicetool[0]:
        num1 = int(input("Input a number: "))
        num2 = int(input("Input another number: "))
        op = input("Input the operation (+, -, /, *): ")

        if op == "+":
            add(num1, num2)
        elif op == "-":
            sub(num1, num2)
        elif op == "/":
            div(num1, num2)
        elif op == "*":
            mul(num1, num2)
        else:
            print("Invalid operation.")

    elif choicetooluser == choicetool[1]:
        convtemp(c)

    elif choicetooluser == choicetool[2]:
        convspeed(kmh)

    elif choicetooluser == choicetool[3]:
        passchecker("")

    elif choicetooluser == choicetool[4]:
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        choicestaskuser = int(input("Choose an option: "))

        if choicestaskuser == 1:
            taskadd()
        elif choicestaskuser == 2:
            taskremove()
        elif choicestaskuser == 3:
            taskview()
        else:
            print("Invalid option")

    elif choicetooluser == choicetool[5]:
        palchecker()

    elif choicetooluser == choicetool[6]:
        randomnumgame()

    elif choicetooluser == choicetool[7]:
        rps()

    elif choicetooluser == choicetool[8]:
        print("Quitting...")
        quit()

    else:
        print("Invalid choice.")
