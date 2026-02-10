# WAP to count all letters (english alphabets), digits and other symbols in a string.

import string

def countCharacters(s):
    letters = 0
    digits = 0
    symbols = 0
    
    alphabetSet = set(string.ascii_letters)
    digitsSet = set(string.digits)
    
    for char in string:
        if char in alphabetSet:
            letters += 1
        elif char in digitsSet:
            digits += 1
        else:
            symbols += 1
            
string1 = input("Enter your string:")

counts = countCharacters(string1)

print(f"Original string: '{string1}")
print(f"Number of letters: {counts['letters']}")
print(f"Number of digits: {counts['digits']}")
print(f"Number of symbols: {counts['symbols']}")