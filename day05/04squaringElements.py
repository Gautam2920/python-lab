# WAP to turn every element of a list into its square

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List", list)

for i in range(len(list)):
    list[i] = list[i] ** 2
    
print("Sqaured List:", list)