# Function to remove first and last character from a string using slicing
def sliceString(s):
    # s[1:-1] means: start from index 1, end at index -1 (last character, exclusive)
    # This removes the first character (index 0) and the last character
    return s[1:-1]

'''
STRING SLICING EXAMPLES:
- s[1:-1] for "hello" returns "ell" (removes 'h' and 'o')
- s[::−1] reverses the string
- s[start:end:step] - start:index, end:index, step:increment/decrement
'''
