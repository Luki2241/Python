# declares username, password and tries
password = "123Banana"
username = "Banana"
guessu = ""
guess = ""
tries = 0
triesu = 0

#checks if the username is correct and stops the program if the tries are too many
while guessu != username:
    guessu = input("Enter your username:")    
    if guessu == username:
        break
    else:
        print("Wrong username try again.")
        triesu += 1
    if triesu == 3:
        print("Access denied.")
        quit()
        
#checks if the password is correct and stops the program if the tries are too many
while guessu == username:
    while guess != password:
        guess = input("Enter your password:")
        if guess == password:
            print("Welcome back!")  
            quit()
        else:
            print("Wrong password try again.")
            tries += 1
        if tries == 3:
            print("Access denied.")
            quit()