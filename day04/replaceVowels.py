# WAP to replace all vowels (lowecase and uppercase) with * in a string.

import re

string1 = input("Enter your string: ")

vowels = "aeiouAEIOU"
replace = "*"

result = re.sub(r'[aeiouAEIOU]', replace , string1)

print(result)