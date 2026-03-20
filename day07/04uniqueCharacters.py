# WAP to count number of unique characters using dictionary

text = input("Enter a string: ")

char_dict = {}

for ch in text:
    if ch not in char_dict:
        char_dict[ch] = 1
    else:
        char_dict[ch] += 1

print("Unique characters: ", len(char_dict))