# --- Arithmetic Operators ---
x = 9
y = 4
print(f"Division: {x/y}")       # Float division (9/4 = 2.25)
print(f"Floor Div: {x//y}")     # Integer division (9//4 = 2, ignores remainder)
print(f"Modulus: {x%y}")        # Remainder (9%4 = 1)
print(f"Power: {x**y}")         # Exponentiation (9**4 = 6561)

''' 
OPERATOR PRECEDENCE (highest at bottom):
+ -         (addition, subtraction)
* / //      (multiplication, division, floor division)
**          (exponentiation)

ASSOCIATIVITY (for operators with same precedence):
+ - (left to right)      : 5 - 3 + 2 = (5-3) + 2 = 4
* / // (left to right)   : 10 / 2 * 5 = (10/2) * 5 = 25
** (right to left)       : 2**3**2 = 2**(3**2) = 2**9 = 512

NOTE: Parentheses always have highest priority and override order
'''

# --- Logical Operators ---
# 'and', 'or', 'not' with short-circuiting behavior.
a = 10
b = 20
c = 30
print(f"a<b and b<c: {a<b and b<c}")
print(f"a<c or c<b: {a<c or c<b}")
print(f"not a>b: {not a>b}")

# Short-circuit examples
s1 = ""  # Empty string is falsy
s2 = s1 or "defaultStr"  # Since s1 is falsy, returns first truthy value: "defaultStr"
print(f"Short-circuit OR: {s2}")

z = 40
print(f"Short-circuit AND: {z and 50}")  # Both truthy, returns last truthy value: 50
# Short-circuiting: if first value is falsy, second value won't be evaluated


# --- Identity Operators ---
# 'is' checks if two variables point to the same object in memory.
x = 10
y = x
print(f"x is y: {x is y}")
print(f"x is not y: {x is not y}")

'''
IDENTITY vs EQUALITY:
- 'is' compares memory addresses (object identity)
- '==' compares values
For containers (lists, tuples): even identical values give 'is' = False
because they are different objects in memory
'''

# --- Membership Operators ---
# 'in' checks if a value exists within a sequence (string, list, etc).
s = "geeksforgeeks"
print(f"'g' in s: {'g' in s}")
print(f"'gk' in s: {'gk' in s}")

'''
MEMBERSHIP with strings:
- Checks for substrings (characters in continuous order)
- Not just individual characters
For dictionaries: checks keys, not values
'''

# --- Bitwise Operators ---
# Operating on binary representations of integers.
print(f"Binary of 18: {bin(18)}")  # bin() converts to binary string '0b10010'
print(f"Int of binary 10010: {int('0b10010', 2)}")  # int() converts back to decimal

# Left Shift (<<)
x = 5  # Binary: 101
print(f"5 << 1: {x<<1}")  # Shift left 1: 1010 = 10 (multiply by 2^1)
print(f"5 << 2: {x<<2}")  # Shift left 2: 10100 = 20 (multiply by 2^2)

# << shifts the binary representation left, filling right with zeros
# Left shift by n equals multiplying by 2^n