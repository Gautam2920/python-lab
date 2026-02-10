# WAP to check whether a string is Palindrome or not.

string1 = input("Enter your string:")

i , j = 0 , len(string1) - 1
isPalindrome =  True

while i < j:
    if string1[i] != string1[j]:
        isPalindrome = False
        break
    i+= 1
    j-= 1
    
if isPalindrome:
    print(string1 , "is a Palindrome.")
else:
    print(string1 , "is not a Palindrome.")