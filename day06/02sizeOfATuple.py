# Write a program to find the size of a tuple

import sys

elements = input("Enter elements seperated by space: ").split()
t = tuple(elements)

print("Tuple: ", t)
print("Size of tuple: ", sys.getsizeof(t))