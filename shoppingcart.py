#defines variables(items)
store_items = {"pizza", "milk", "water", "apple"}
cart = set()
options = [1, 2, 3, 4, 5]
optionitem = ""
#defines functions
def additem():
    print("Items available:", store_items)
    optionitem = input("Which item do you wanna add?: ").lower()
    cart.add(optionitem)
def removeitem():
    print("Items in your cart:", cart)
    optionitem = input("Which item do you wanna remove?: ").lower()
    cart.remove(optionitem)
print("What do you want to do?")
print()
#main loop
while True:
    print("1. Add items")
    print()
    print("2. Remove items")
    print()
    print("3. Show items available")
    print()
    print("4. Show items in cart")
    print()
    print("5. Exit")
    #asks user for input
    optionuser = int(input("Choose an option:"))
    
    if optionuser == options[0]:
        additem()
        print("Item added!")
    elif optionuser == options[1]:
        if cart == len(cart) == 0:
                print("No items in your cart right now.")
        else:
            removeitem()
    
    elif optionuser == options[2]:
        print("The items available are:", store_items) 
    
    elif optionuser == options[3]:
        if cart == len(cart) == 0:
            print("There are no items in your cart!")
        else:    
            print("Your items in your cart right now are:", cart)
            
    elif optionuser == options[4]:
        print("Quitting...")
        quit()       
        
    else:
        print("Invalid option.")