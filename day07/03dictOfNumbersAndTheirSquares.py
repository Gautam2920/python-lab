# WAP to generate dictionary of numbers and their squares (i, i*i) from 1 to N

num = int(input("Enter a number: "))

squares = {i: i*i for i in range(1, num+1)}

print("Dictionary of numbers and their squares: ", squares)