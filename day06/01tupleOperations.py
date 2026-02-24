# Write a program to demonstrate various tuple operations in python.

# Creating a tuple
t = {1, 2, 3, 4, 5}

# Accessing elements
print("Fisrt element: ", t[0])
print("Second element: ", t[1])

# Slicing tuple
print("Sliced tuple from 1 to 3: ", t[1:4])

# Concatenation
t2 = {6, 7, 8}
print("Concatenated t and t2", t+t2)

# Repetition
print("Tuple t2 repeated 3 times: ", t2 * 3)

# Length of a tuple
print("Length of tuple t:", len(t))

# Checking membership
print("Is 30 present in t?", 30 in t)

# Iterating through tuple
print("Elements in t:")
for item in t:
    print(item)