'''palindrome example-
abba is equal to abba'''
s=input("Enter the string:")
low=0 #compare the initial character of string
high=len(s)-1 # To the last character (-1 is to match with the index of the characters in the string)
while low<high:
    if s[low]!=s[high]:
        print("Not a palindrome")
        break
    low=low+1
    high=high-1
else:
    print("palindrome")

#OR (simple method)

if s==s[::-1]: # s[::-1] would get the reverse of any string which is a shortcut method as discussed in reverse_string.py previously
    print("palindrome")
else:
    print("Not a palindrome")

def isPalindrome(s):
    #code here
    return s[::-1].lower() == s.lower() # to ignore lower and upper case and just check if it's palindrome and return t/f