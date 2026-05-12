# WAP to illustrate handling of Type exception.

try:
    num = 10
    text = "Hello"

    result = num + text
    print(result)

except TypeError:
    print("Error: Unsupported operation between different data types.")