# WAP to Merge two tuples and remove duplicates.

t1 = tuple(input("Enter elements of first tuple seperated by space").split())
t2 = tuple(input("Enter elements of second tuple seperated by space").split())

merged = tuple(set(t1 + t2))

print("Merged tuple without duplicates:", merged)