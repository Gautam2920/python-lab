# WAP to illustrate handling of ValueError Exception.

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    print("Error: Invalid input. Please enter only numbers.")