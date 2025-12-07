def calc(operation, *numbers):
    if not numbers:
        return "No number provided."
        
    elif operation == "add":
        return sum(numbers)
        
    elif operation == "subtract":
        result = numbers[0]
        for n in numbers[1:]:
            result -= n
        return result            
    
    elif operation == "multiply":
        result = 1
        for n in numbers:
            result *= n
        return result            
        
    elif operation == "divide":
        result = numbers[0]
        for n in numbers[1:]:
            if n == 0:
                return "You cannot divide by zero."
            result /= n
        return result            

print(calc("divide",4 ,5 ,2))