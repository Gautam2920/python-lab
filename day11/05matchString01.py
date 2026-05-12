# WAP to match a string that contains only upper and lowercase letters, numbers, and underscores

import re

text = input("Enter a string: ")

pattern = "^[A-Za-z0-9_]+$"

if re.match(pattern, text):
    print("Valid string")
else:
    print("Invalid string")