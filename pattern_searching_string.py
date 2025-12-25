# Get text and pattern from user
txt = input("Enter the text: ")
pat = input("Enter the pattern: ")

# Find all positions where the pattern occurs in the text
pos = txt.find(pat)  # Returns index of first occurrence, or -1 if not found
while pos >= 0:  # While pattern is found (pos is not -1)
    print(pos)  # Print the position/index of pattern found
    pos = txt.find(pat, pos + 1)  # Search for next occurrence starting from pos+1


