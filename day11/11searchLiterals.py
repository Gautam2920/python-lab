# WAP to search some literals strings in a string.

import re

text = "Python is easy and Python is powerful"

pattern = "Python"

result = re.findall(pattern, text)

print("Occurrences found:", len(result))