# Find the second largest element in a tuple.

elements = list(map(int, input("Enter elements seperated by space").split()))
t = tuple(elements)

unique_sorted = sorted(set(t))

if(len(unique_sorted) < 2):
    print("Second largest element does not exist.")
else:
    print("Second largest element:", unique_sorted[-2])