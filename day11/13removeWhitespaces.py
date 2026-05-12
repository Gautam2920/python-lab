# WAP to remove all whitespaces from a string.

import re

text = input("Enter a string: ")

result = re.sub(r"\s+", "", text)

print("String without spaces:")
print(result)