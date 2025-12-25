'''
DECIMAL TO BINARY CONVERSION EXAMPLES:
17 in decimal = 10001 in binary
  Powers of 2: 1×16 + 0×8 + 0×4 + 0×2 + 1×1 = 17

12 in decimal = 1100 in binary
  Powers of 2: 1×8 + 1×4 + 0×2 + 0×1 = 12

15 in decimal = 1111 in binary
  Powers of 2: 1×8 + 1×4 + 1×2 + 1×1 = 15
'''

# --- Method 1: Manual conversion using modulo and division ---
def decToBinary(n):
    if n == 0:  # Special case: 0 in decimal is 0 in binary
        return "0"
    res = ""  # String to store binary digits
    while n > 0:
        res = res + str(n % 2)  # Get last binary digit (n%2 is 0 or 1)
        n = n // 2  # Integer divide by 2 to process next digit
    return res[::-1]  # Reverse the string because digits were added backwards

# --- Method 2: Using built-in bin() function ---
def decToBin(n):
    res = bin(n)  # bin() returns string like '0b10001' for 17
    return res[2:]  # Remove '0b' prefix by slicing from index 2 onwards

