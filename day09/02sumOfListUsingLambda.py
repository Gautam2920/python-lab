# WAP to find the sum of elements of a list using lambda function.

from functools import reduce

nums = [1, 2, 3, 4, 5]

total = reduce(lambda x, y: x + y, nums)

print("Sum:", total)