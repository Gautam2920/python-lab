# WAP to validate a 10-digit mobile number.

import re

mobile = input("Enter mobile number: ")

pattern = "^[0-9]{10}$"

if re.match(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")