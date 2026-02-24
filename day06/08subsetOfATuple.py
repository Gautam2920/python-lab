# Check if a tuple is a subset of another tuple.

t1 = tuple(input("Enter elements of first tuple seperated by space").split())
t2 = tuple(input("Enter elements of second tuple seperated by space").split())

if set(1).issubset(set(t2)):
    print("First tuple is a subset of second tuple.")
else:
    print("First tuple is not a subset of second tuple.")