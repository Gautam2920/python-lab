# WAP to demonstrate working with dictionaries in python.

# Creating a dictionary
student = {
    "name": "Arjun",
    "age": 20,
    "branch": "Engineering",
    "cgpa": 8.7
}

print("Original Dictionary:")
print(student)

# Accessing values
print("\nAccessing Values:")
print("Name:", student["name"])
print("CGPA:", student.get("cgpa"))

# Adding a new key-value pair
student["year"] = 2
print("\nAfter Adding 'year':")
print(student)

# Updating a value
student["cgpa"] = 9.0
print("\nAfter Updating CGPA:")
print(student)

# Removing an item
removed_value = student.pop("age")
print("\nRemoved 'age':", removed_value)
print("After Removal:")
print(student)

# Looping through dictionary
print("\nLooping Through Dictionary:")
for key, value in student.items():
    print(key, ":", value)

# Dictionary methods
print("\nDictionary Keys:", student.keys())
print("Dictionary Values:", student.values())
print("Dictionary Items:", student.items())

# Clearing dictionary
temp_dict = student.copy()
temp_dict.clear()
print("\nAfter Clearing Copied Dictionary:")
print(temp_dict)