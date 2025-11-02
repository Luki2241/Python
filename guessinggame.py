#imports random and generates a random number
import random
number = random.randint(1, 10)

#gives the player 3 tries to guess the number
for i in range (3):
    gnumber = int(input("Input a number to guess:"))
    if gnumber == number:
         print("Correct!")  
         quit() 
    else:
        print("Wrong number try again.")