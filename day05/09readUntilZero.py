# WAP that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the  values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line.

numbers = []

while True:
    num = int(input("Enter numbers (0 to stop):"))
    if num == 0:
        break
    numbers.append(num)
    
numbers.sort()

print("Numbers in ascending order:", numbers)