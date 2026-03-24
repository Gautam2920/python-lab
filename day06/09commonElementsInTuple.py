# WAP to Find the common elements between two tuples.

t1 = tuple(input("Enter elements of first tuple seperated by space").split())
t2 = tuple(input("Enter elements of second tuple seperated by space").split())

common = tuple(set(t1) & set(t2))

print("Common elements: ", common)