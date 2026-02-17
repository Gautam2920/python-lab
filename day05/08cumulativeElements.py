# WAP to find the cumulative sum of elements in a list

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    list.append(int(input(f"Enter element {i+1}:")))
    
print("Original List", list)

cumulative_sum = []
total = 0

for num in list:
    total+= num
    cumulative_sum.append(total)
    
print("Cumulative sum list", cumulative_sum)