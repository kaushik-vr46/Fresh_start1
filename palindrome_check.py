'''
PALINDROME EXAMPLES:
A palindrome reads the same forwards and backwards.
Examples: "abba", "racecar", "noon"
'''

# Get string input from user
s = input("Enter the string: ")

# --- Method 1: Two-pointer comparison (manual) ---
low = 0  # Pointer at the beginning
high = len(s) - 1  # Pointer at the end (-1 because indices start at 0)
while low < high:  # Compare characters from outside towards center
    if s[low] != s[high]:  # If characters don't match
        print("Not a palindrome")
        break  # Stop checking
    low = low + 1  # Move start pointer right
    high = high - 1  # Move end pointer left
else:  # This else runs if the while loop completes without break
    print("Palindrome")

# --- Method 2: Simple string reversal (cleaner) ---
if s == s[::-1]:  # s[::-1] reverses the string
    print("Palindrome")
else:
    print("Not a palindrome")

# --- Method 3: Function with case-insensitive check ---
def isPalindrome(s):
    # Compare lowercase version with its reverse (ignores case)
    return s[::-1].lower() == s.lower()