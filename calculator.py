num1 = int(input("Input a number:"))

num2 = int(input("Input another number:"))

op = input("Input the operation (+, -, /, *):")

if op == "+":
    print(num1 + num2)
    
elif op == "-":
    print(num1 - num2)

elif op == "/":
    print(num1 / num2)
    
elif op == "*":
    print(num1 * num2)

else:
    print("Invalid operation.")    