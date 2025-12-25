# --- Method 1: Using a loop to build reversed string ---
s = input("Enter the string: ")
rev = ""  # Empty string to store reversed characters
for i in s:  # Iterate through each character
    rev = i + rev  # Prepend current character to the result
print(rev)  # Print the reversed string

'''
LOOP EXAMPLE for input="abcd":
Loop 1: i='a' then rev='a'+'' = 'a'
Loop 2: i='b' then rev='b'+'a' = 'ba'
Loop 3: i='c' then rev='c'+'ba' = 'cba'
Loop 4: i='d' then rev='d'+'cba' = 'dcba'
Output: 'dcba'
'''

# --- Method 2: Using slicing (shorter, preferred) ---
'''
s = input("Enter the string: ")
print(s[::-1])

String slicing syntax: s[start:end:step]
- s[::−1] means: start from end, go to beginning, step by -1 (reverse)
Example: "hello"[::-1] = "olleh"
'''
