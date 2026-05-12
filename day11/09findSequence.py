# WAP to find the sequences of one upper case letter followed by lower case letters. 

import re

text = input("Enter a string: ")

pattern = "[A-Z][a-z]+"

result = re.findall(pattern, text)

print("Matches:", result)