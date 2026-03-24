# WAP to Find the frequency of each element in a tuple.

elements = list(map(int, input("Enter elements seperated by space").split()))
t = tuple(elements)

frequency = {}

for item in t:
    frequency[item] = frequency.get(item, 0) + 1
    
print("Frequency of each element:")
for key, value in frequency.items():
    print(key, ":", value)    