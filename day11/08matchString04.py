# WAP that matches a string that has an a followed by three 'b'.

import re

text = input("Enter a string: ")

pattern = "^ab{3}$"

if re.match(pattern, text):
    print("Match found")
else:
    print("No match")