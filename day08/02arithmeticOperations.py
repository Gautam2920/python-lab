# WAF to calculate the arithmetic operation on two number using user defined values.

def arithmeticOperations() :
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    sum = num1 + num2
    print("The sum of", num1, "and", num2, "=", sum)

    difference = num1 - num2
    print("The differnece of", num1, "and", num2, "=", difference)
    
    product = num1 * num2
    print("The product of", num1, "and", num2, "=", product)
    
    if(num2 == 0) :
        print("Division by 0 is not possible.")
    else :
        quotient = num1 / num2
        print("The quotient of", num1, "and", num2, "=", quotient)
    
    
arithmeticOperations()