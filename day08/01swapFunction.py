# WAF to write user defined function to swap two numbers and display number

def swap():
    num1 = int(input("Enter first number num1: "))
    num2 = int(input("Enter second number num2: "))
    print("Before swap, num1 = ", num1, "num2 = ", num2)
    
    temp  = num1
    num1 = num2
    num2 = temp
    
    print("After swap, num1 = ", num1, "num2 = ", num2)
    
swap()