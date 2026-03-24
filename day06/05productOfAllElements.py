# WAP to Find the product of all elements in a tuple.

elements = list(map(int, input("Enter elements seperated by space").split()))
t = tuple(elements)

product = 1
for num in t:
    product*= num
    
print("Product of elements in the tuple:", product)