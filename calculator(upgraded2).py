#declares variables and all the functions
ops = ["+", "-", "/", "*"]
options = ["yes", "no"]
result = 0

def add():
    print(num1 + num2)
    result = num1 + num2
    print(num1, op, num2, "=", result)
    return
def sub():
    print(num1 - num2)
    result = num1 - num2
    print(num1, op, num2, "=", result)
    return
def div():
    if num2 == 0:
        print("Invalid operation.")
    else:
        print(num1 / num2)
        result = num1 / num2
        print(num1, op, num2, "=", result)
        return
def mul():
    print(num1 * num2)
    result = num1 * num2
    print(num1, op, num2, "=", result)
    
#main loop
while True:
    num1 = int(input("Input a number:"))

    num2 = int(input("Input another number:"))
    
    op = input("Input the operation (+, -, /, *):")
    
    if op == ops[0]:
        add()
        
    elif op == ops[1]:
        sub()
        
    elif op == ops[2]:
        div()
    
    elif op == ops[3]:
        mul()
        
    else:
        print("Invalid operation.")    
        
    #asks user if they want to continue calculating
    optionuser = input("Do you wanna calculate something else?: ").lower()
        
    if optionuser == options[0]:
        continue
        
    elif optionuser == options[1]:
        print("Quitting...")
        quit()
            
    else: 
        print("Invalid option.")
        continue