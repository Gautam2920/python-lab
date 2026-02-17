# WAP to interchange first and last element of a list

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List:", list)
    
if len(list) > 0:
    list[0] , list[-1] = list[-1], list[0]
    
print("Updated list:", list)