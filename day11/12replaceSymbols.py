# WAP to replace whitespaces with an underscore and vice versa.

import re

text = input("Enter a string: ")

result1 = re.sub(" ", "_", text)
print("Spaces replaced with underscores:")
print(result1)

result2 = re.sub("_", " ", text)
print("Underscores replaced with spaces:")
print(result2)