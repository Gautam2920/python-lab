# WAP to find small number between two numbers using Lambda function.

small = lambda a, b: a if a < b else b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Smallest number:", small(num1, num2))