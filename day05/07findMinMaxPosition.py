# WAP to find the position of Minimum and Maximum elements in a list

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List", list)

min_value = min(list)
max_value = max(list)

print("Minimum value is", min_value , "at index", list.index(min_value))
print("Maximum value is", max_value , "at index", list.index(max_value))