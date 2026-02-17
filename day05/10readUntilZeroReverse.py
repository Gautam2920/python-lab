# WAP that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your  program should display them (except for the 0) in reverse order

numbers = []

while True:
    num = int(input("Enter numbers (0 to stop):"))
    if num == 0:
        break
    numbers.append(num)
    
numbers.sort()

print("Numbers in ascending order:")
for num in reversed(numbers):
    print(num)