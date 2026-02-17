# WAP to replace list's item with new value if found

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List", list)

old_value = int(input("Enter value to replace:"))
new_value = int(input("Enter new value:"))

for i in range(len(list)):
    if list[i] == old_value:
        list[i] == new_value
        
print("Updated List:", list)