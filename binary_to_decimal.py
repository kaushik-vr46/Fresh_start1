'''
BINARY TO DECIMAL CONVERSION EXAMPLES:
110 in binary = 6 in decimal
  Calculation: 1×4 + 1×2 + 0×1 = 4 + 2 = 6

10001 in binary = 17 in decimal
  Calculation: 1×16 + 0×8 + 0×4 + 0×2 + 1×1 = 16 + 1 = 17
'''

# --- Method 1: Manual approach using powers of 2 ---
def binToDec(b):
    res = 0  # Initialize result
    p = 1  # Power of 2, starts at 2^0 = 1
    for x in reversed(b):  # Start from rightmost digit by reversing the string
        res = res + int(x) * p  # Add (digit × current power of 2) to result
        p = p * 2  # Move to next power of 2 (multiply by 2 each iteration)
    return res

# --- Method 2: Using built-in function (Simpler) ---
def binToDec2(b):
    # int(b, 2) interprets the string 'b' as binary (base 2) and converts to decimal
    res = int(b, 2)
    return res

# Get binary input from user
n = input()

# Print decimal output using both methods
print(binToDec2(n))  # Output using built-in function
print(binToDec(n))   # Output using manual calculation
