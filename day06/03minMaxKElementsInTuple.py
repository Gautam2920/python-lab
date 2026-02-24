# Write a program to find the maximum and minimum K elements in a tuple

elements = list(map(int, input("Enter elements seperated by space").split()))
t = tuple(elements)

k = int(input("Enter value of K: "))

sorted_t = sorted(t)

print("Minimum K elements:", sorted_t[:k])
print("Maximum K elements: ", sorted_t[-k:])