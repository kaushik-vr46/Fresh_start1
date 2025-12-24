# --- Arithmetic Operators ---
x = 9
y = 4
print(f"Division: {x/y}")       # Float division
print(f"Floor Div: {x//y}")     # Integer division
print(f"Modulus: {x%y}")        # Remainder
print(f"Power: {x**y}")         # Exponentiation

''' 
+ - 
* / //
**
above are the order of precedence with bottom most being the highest precedence
In case of same precedence operators being in the operation the associativity is:
+ - (left to right)
* / // (left to right)
** (right to left)
PS- not matter the associativity order, if anything is in brackets, it would be solved first
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
s1 = ""
s2 = s1 or "defaultStr" # if s1 empty goes to defaultstr value, if s1 not empty it would go to s1 value (prints non zero string/integer value)
print(f"Short-circuit OR: {s2}")

z = 40
print(f"Short-circuit AND: {z and 50}") # prints the last executed value if z is non zero value, prints 0 if z is zero value and second value
#will not be executed, this is called short circuiting


# --- Identity Operators ---
# 'is' checks if two variables point to the same object in memory.
x = 10
y = x
print(f"x is y: {x is y}")
print(f"x is not y: {x is not y}")

'''compares values of id values for the variable and returns boolean values (true or false), for containers like list or tuples we won't get true as output even if they are
the same and we would get the output to be false only'''

# --- Membership Operators ---
# 'in' checks if a value exists within a sequence (string, list, etc).
s = "geeksforgeeks"
print(f"'g' in s: {'g' in s}")
print(f"'gk' in s: {'gk' in s}")

'''only to see if the  substrings (characters in continous order in the main string) are there in strings and for strings only
also checks for key and value for dictionary'''

# --- Bitwise Operators ---
# Operating on binary representations of integers.
print(f"Binary of 18: {bin(18)}")
print(f"Int of binary 10010: {int('0b10010', 2)}")

# Left Shift (<<)
x = 5
print(f"5 << 1: {x<<1}")
print(f"5 << 2: {x<<2}")

# << shifts the binary representation of a number to the left by a specified number of positions, filling the right side with zeros