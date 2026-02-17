# WAP to find even numbers from a list

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List", list)
    
even_numbers = []

for num in list:
    if num % 2 == 0:
        even_numbers.append(num)

print("List of even numbers from original list:", even_numbers)