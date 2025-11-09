while True:
    word = input("Enter a word:").lower()
    reversedword = word[::-1]
    print("Reversed word:", reversedword)
    if reversedword == word:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")
    option = input("Do you wanna check another word?: ").lower()
    if option == "yes":
        pass
    elif option == "no":
        print("Quitting...")
        quit()
    else:
        print("Invalid option.")
        quit()    