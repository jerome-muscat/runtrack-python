def calcule(num1, operator, num2):
    if operator == "+":
        print(num1 + num2)

    elif operator == "-": 
        print(num1 - num2)
    
    elif operator == "*":
        print(num1 * num2)
    
    elif operator == "/":
        print(num1 / num2)
        
    elif operator == "%":
        print(num1 % num2)

calcule(40, "+", 10)
calcule(38, "-", 286)
calcule(67, "*", 556)
calcule(90, "/", 50)
calcule(48, "%", 87)