# WAP to check whether a number is an armstrong number.

num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** digits
    temp //= 10

if armstrong_sum == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
