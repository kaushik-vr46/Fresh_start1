import math

# --- Count Digits in a Number ---
print("--- Count Digits ---")
x = int(input("Enter number to count digits: "))
temp_x = x  # Keep original value
res = 0  # Counter for digits
while temp_x > 0:
    temp_x = temp_x // 10  # Remove last digit
    res = res + 1  # Increment digit count
print(f"Digits: {res}")


# --- Factorial (n!) ---
print("\n--- Factorial ---")
n = int(input("Enter number for factorial: "))
res = 1  # Initialize result
for i in range(2, n + 1):  # Multiply from 2 to n
    res = res * i
print(f"Factorial (Loop): {res}")
print(f"Factorial (Math Lib): {math.factorial(n)}")  # Using built-in function


# --- GCD (Greatest Common Divisor) and LCM ---
print("\n--- GCD & LCM ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# --- Method 1: Manual GCD calculation using loop ---
small = min(a, b)  # GCD cannot be larger than the smaller number
gcd_val = 1  # Start with 1 (always a common divisor)
for i in range(1, small + 1):  # Check all numbers up to smaller value
    if a % i == 0 and b % i == 0:  # If both divisible by i
        gcd_val = i  # Update GCD (this keeps the largest)
print(f"GCD (Loop): {gcd_val}")
print(f"GCD (Math Lib): {math.gcd(a, b)}")  # Using built-in function

# --- LCM (Least Common Multiple) ---
# Formula: LCM(a,b) = (a * b) / GCD(a,b)
lcm = (a * b) // gcd_val
print(f"LCM: {lcm}")


# --- Fibonacci Series ---
print("\n--- Fibonacci Series ---")
n = int(input("Enter n for Fibonacci: "))
if n == 0:
    print(1)
elif n == 1:
    print(1, 1)
else:
    print(1, 1, end=" ")  # Print first two terms
    a, b = 1, 1  # Initialize for Fibonacci
    for i in range(2, n + 1):  # Generate remaining terms
        c = a + b  # Next term is sum of previous two
        print(c, end=" ")
        a = b  # Move forward
        b = c
    print()