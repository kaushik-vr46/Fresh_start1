'''
--- Traditional (SLOWER) version of prime number check and divisor finding ---
This demonstrates a less efficient approach for reference purposes.

SLOWER PRIME CHECK:
- Checks ALL numbers from 2 to n-1 = O(n) time complexity
- Has a bug: prints "Yes" multiple times instead of once

SLOWER DIVISOR CHECK:
- Checks ALL numbers from 1 to n
- Less efficient than the optimized approach
'''

# --- All Divisors (Optimized) ---
n = int(input("Enter a number to check: "))

print(f"--- Divisors of {n} ---")
x = 1
# Check only up to √n because divisors come in pairs
# If x divides n, then (n/x) also divides n
while x * x < n:
    if n % x == 0:  # If x divides n
        print(x)  # Print first divisor
        print(n // x)  # Print corresponding pair divisor (n/x)
    x = x + 1
if x * x == n:  # Check if n is a perfect square
    print(x)  # If perfect square, x is a divisor printed once


# --- Prime Number Check (Optimized) ---
print(f"\n--- Is {n} Prime? ---")
if n <= 1:
    print("No")  # 0, 1, and negatives are not prime
else:
    x = 2
    is_prime = True
    # Optimization: Check only up to square root of n
    # If n has a divisor > √n, it must also have a divisor < √n
    # Example: For n=31, only check up to √31 ≈ 5.6
    # If 31 is not divisible by 2,3,4,5 then it's definitely prime
    while x * x <= n:  # Only check divisors up to √n
        if n % x == 0:  # If divisible by x, then n is NOT prime
            print("No")
            is_prime = False
            break
        x = x + 1
    
    if is_prime:
        print("Yes")

'''
TIME COMPLEXITY COMPARISON:
SLOW approach: O(n) - checks 2 to n-1
- For n=1,000,000: checks 999,998 numbers

OPTIMIZED approach: O(√n) - checks 2 to √n
- For n=1,000,000: checks only ~1,000 numbers

That's approximately 1000x faster!
'''