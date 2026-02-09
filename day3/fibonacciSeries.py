# WAP to print fibonacci series.

n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
else:
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
