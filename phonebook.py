#declares variables and functions
contacts = {}
addconname = ""
addconnumber = 0
removeconname = ""
searchcon = ""
options = [1, 2, 3, 4, 5]
optionuser = 0
def addcontact():
    addconname = input("Enter the contact name you wanna add: ")
    addconnumber = int(input("Enter your contacts number: "))
    contacts[addconname] = addconnumber
    
def removecontact():
    removeconname = input("Enter the contact name you wanna remove:")
    if removeconname in contacts and len(contacts) > 0:
        contacts.pop(removeconname)
    else:
        print("Contact not found or no contacts.")
        
def searchcontacts():
    if len(contacts) > 0:
        searchcon = input("Search your contact: ")
        if searchcon in contacts:
            contacts.get(searchcon)
        else:
            print("Contact not found.")
    else:
        print("No contacts")

def viewcontacts():
    print(contacts.items())
    
while True:
    print("1. Add contacts")
    print("2. Remove contacts")
    print("3. Search contacts")
    print("4. Show all contacts")
    print("5. Exit")
    optionuser = int(input("Enter an option: "))
    
    if optionuser == options[0]:
        addcontact()             
        
    elif optionuser == options[1]:
        removecontact()
        
    elif optionuser == options[2]:
        searchcontacts()
        
    elif optionuser == options[3]:
        viewcontacts()
        
    elif optionuser == options[4]:
        print("Quitting...")
        quit()
        
    else:
        print("Invalid option.")