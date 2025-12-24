import math

# --- Count Digits ---

print("--- Count Digits ---")
x = int(input("Enter number to count digits: "))
temp_x = x
res = 0
while temp_x > 0:
    temp_x = temp_x // 10
    res = res + 1
print(f"Digits: {res}")


# --- Factorial ---

print("\n--- Factorial ---")
n = int(input("Enter number for factorial: "))
res = 1
for i in range(2, n + 1):
    res = res * i
print(f"Factorial (Loop): {res}")
print(f"Factorial (Math Lib): {math.factorial(n)}")


# --- GCD (Greatest Common Divisor) ---

print("\n--- GCD & LCM ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Manual calculation

small = min(a, b)
gcd_val = 1
for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd_val = i
print(f"GCD (Loop): {gcd_val}")
print(f"GCD (Math Lib): {math.gcd(a, b)}")

# --- LCM (Least Common Multiple) ---

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
    print(1, 1, end=" ")
    a, b = 1, 1
    for i in range(2, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
    print()