# WAF that takes three numbers as parameters, and returns the median value. Include a main program that reads values from user and displays the median.

def median(a, b, c) :
    if(a >= b and a <= c) or (a <= b and a >= c) :
        return a
    elif(b >= a and b <= c) or (b <= a and b >= c) :
        return b
    else :
        return c
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("The median of", num1, num2, num3, "=", median(num1, num2, num3))