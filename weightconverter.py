option = "yes"
while option == "yes":
    weightk = int(input("Enter your weight in kg: "))
    weightl = weightk * 2.205
    print("Your weight in lb is: ", weightl)
    
    option = input("Do you want to convert another weight?: ").lower()
    if option == "yes":
        pass
    elif option == "no":
        print("Quitting...")
        quit()
    else:
        print("Invalid option")