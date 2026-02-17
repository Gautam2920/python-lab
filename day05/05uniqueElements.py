# WAP to check all elements are unique or not in Python

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List", list)

if len(list) == len(set(list)):
    print("All elements are unique")
else:
    print("Duplicate elements exits")