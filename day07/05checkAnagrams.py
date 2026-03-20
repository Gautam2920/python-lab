# WAP to check whether two strings are anagrams using dictionary

str1 = input("Enter first word: ").lower()
str2 = input("Enter second word: ").lower()

if len(str1) != len(str2):
    print("The strings are not Anagrams")
else:
    char_count = {}

    for ch in str1:
        char_count[ch] = char_count.get(ch, 0) + 1

    for ch in str2:
        if ch in char_count:
            char_count[ch] -= 1
            if char_count[ch] == 0:
                del char_count[ch]
        else:
            print("The strings are not Anagrams")
            break
    else:
        if len(char_count) == 0:
            print("The strings are Anagrams")
        else:
            print("The strings are not Anagrams")