# WAP that matches a string that has an a followed by zero or more b's.

import re

text = input("Enter a string: ")

pattern = "^ab*$"

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")