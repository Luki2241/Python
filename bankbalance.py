balance = 0
option = ""


while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")
    option = int(input("Enter option: "))
    if option == 1: 
        amount = int(input("Amount to deposit: "))
        balance += amount
    elif option == 2:
        amount = int(input("Amount to withdraw:"))
        balance -= amount
        if amount > balance:
            print("Not enough funds!")
            balance += amount
    elif option == 3:
        print("Your balance is:", balance)
    elif option == 4:
        print ("Thank you for using our bank!")
        quit()
    
    else:
        print("Invalid action.")
        