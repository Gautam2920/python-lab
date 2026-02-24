# Write a program to create a list of tuples from given list having number and its cube in each tuple .

numbers = list(map(int, input("Enter elements seperated by space").split()))

result = [(num, num**3) for num in numbers]

print("List of tuples (number, cube): ", result)