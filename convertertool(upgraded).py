# declares all the variables and functions
choices = [1, 2, 3]
kg = 0
kmh = 0
c = 0
lbs = 0
mph = 0 
f = 0
optionb = ""
def convweight(kg):
    kg = int(input("Enter weight in kg: "))
    lbs = kg * 2.205
    print("The weight in lbs is:", lbs)
    return

def convspeed(kmh):
    kmh = int(input("Enter speed in kmh: "))
    mph = kmh / 1.609344
    print("The speed in mph is:", mph)
    return

def convtemp(c):        
    c = int(input("Enter temperature in C°: "))
    f = c * 1.8 + 32
    print("The temperature in F° is:", f)
    return
    
# main loop and selection screen
while True:
    # asks user for input
    print("1. Convert kg to lbs")
    print("2. Convert km/h to mph")
    print("3. Convert C° to F°")
    option = int(input("Choose a tool(1, 2, 3): "))
    # main program
    if option == choices[0]:
        convweight(kg)
    elif option == choices[1]:
        convspeed(kmh)
    elif option == choices[2]:
        convtemp(c)
    else:
        print("Invalid option.")
        continue
    # asks user if they want to convert something else
    optionb = input("Do you want to convert something else?").lower()
    
    if optionb == "yes":
        continue
    elif optionb == "no":
        print("Quitting...")
        quit()
    else:
        print("Invalid option.")
        continue