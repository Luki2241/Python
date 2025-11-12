#declares variable
options = ["yes", "no"]

#main loop
while True:
    word = input("Enter a word or a sentence: ")
    
    if word == word.lower():
        print("You're calm.")
    
    elif word == word.upper():
        print("You're shouting!")

    elif word == word.capitalize():
        print("Proper word.")
        
    else:
        print("Mixed case!")
        
    #asks user to continue or not
    optionuser = input("Do you wanna type another word?: ").lower()
    
    if optionuser == options[0]:
        continue    
    
    elif optionuser == options[1]:
        print("Quitting...")
        quit()
    
    else:
        print("Invalid option.")
        continue