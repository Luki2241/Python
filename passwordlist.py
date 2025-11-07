passwords = ["apple123", "banana123", "orange123"]
guess = ""
tries = 0

while True:
    guess = input("Enter your password:")
    
    if guess in passwords:
        print("Welcome back!")
        quit()
    else:
        print("Access denied.")
        tries += 1
        
    if tries == 3:
        print("Too many tries!")
        quit()