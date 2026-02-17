# WAP to demonstrate various list operations in python

n = int(input("Enter number of elements:"))
list = []

for i in range(n):
    value = int(input(f"Enter element {i+1}:"))
    list.append(value)
    
print("\n Original List", list)

# appending value in a list
new_element = int(input("Enter value to append:"))
list.append(new_element)
print("\n List after appending", list)

# inserting value in a list
position = int(input("Enter position to insert element:"))
ins_value = int(input("Enter value to insert:"))
list.insert(position , ins_value)
print("List after insertion", list)

# removing value from a list
remove_value = int(input("Enter value to remove:"))
if remove_value in list:
    list.remove(remove_value)
    print("After removing value", list)
else:
    print("Value not available in list")
    
# sorting elements
list.sort()
print("List after sorting elements", list)

# reversing elements
list.reverse()
print("List after reversing", list)