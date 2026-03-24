# WAF that generates a random password. The password should have a random length of between 7 and 10 characters. Each character should be randomly selected from positions 33 to 126 in ASCII table. No input parameters , and password as return value.

import random

def randPass() :
    length = random.randint(7, 10)
    
    password = ""
    
    for _ in range(length) :
        char = chr(random.randint(33, 126))
        password += char
        
    return password

print("Randomly generated password :", randPass())