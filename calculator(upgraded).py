#declares variable
ops = ["+", "-", "/", "*"]
options = ["yes", "no"]
result = 0
#main loop
while True:
    num1 = int(input("Input a number:"))

    num2 = int(input("Input another number:"))
    
    op = input("Input the operation (+, -, /, *):")
    
    if op == ops[0]:
        print(num1 + num2)
        result = num1 + num2
        print(num1, op, num2, "=", result)
        
    elif op == ops[1]:
        print(num1 - num2)
        result = num1 - num2
        print(num1, op, num2, "=", result)
        
    elif op == ops[2]:
        print(num1 / num2)
        result = num1 / num2
        print(num1, op, num2, "=", result)
    
    elif op == ops[3]:
        print(num1 * num2)
        result = num1 * num2
        print(num1, op, num2, "=", result)
        
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