# WAP that reads values from the user until a blank line is entered. Display the values.

def read_values():
    val = input("Enter value (blank to stop): ")
    
    if val == "":
        return []
    
    return [val] + read_values()

values = read_values()
print("Entered values:", values)