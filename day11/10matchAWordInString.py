# WAP that matches a word at the beginning of a string.

import re

text = input("Enter a string: ")

pattern = "^\w+"

result = re.search(pattern, text)

if result:
    print("Matched word:", result.group())
else:
    print("No match found") 