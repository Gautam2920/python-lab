# WAP to filter even values from list using lambda function.

nums = [1, 2, 3, 4, 5, 6, 7, 8]

even_nums = list(filter(lambda x: x % 2 == 0, nums))

print("Even numbers:", even_nums)