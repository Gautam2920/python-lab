# WAP to illustrate handling of Index Error Exception

try:
    numbers = [10, 20, 30, 40]

    index = int(input("Enter index number: "))
    print("Element =", numbers[index])

except IndexError:
    print("Error: Index out of range.")