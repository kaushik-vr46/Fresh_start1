'''
--- Traditional version of prime number check and finding all divisors of a number which is a much slower code and higher computation duration ---
--- START OF EXAMPLE CODE ---

# prime number

if(n<=1):
    print("No")
else:
    for i in range(2,n):
        if(n%i==0):
            print("No")
            break
        else:
            print("Yes")

#all divisors of a number

for x in range(i,n+1):
    if n%x==0:
        print(x)

n = int(input("Enter a number to check: ")) 

--- END OF EXAMPLE CODE ---
'''

# --- All Divisors (Optimized version of above code) ---
n = int(input("Enter a number to check: "))

print(f"--- Divisors of {n} ---")
x = 1
while x * x < n:
    if n % x == 0: # gets both divisors in one step and quicker than the original step
        print(x)          # First divisor
        print(n // x)     # Corresponding pair divisor
    x = x + 1
if x * x == n:            # Perfect square check
    print(x)


# --- Prime Number Check (Optimized version of above code) ---

print(f"\n--- Is {n} Prime? ---")
if n <= 1:
    print("No")
else:
    x = 2
    is_prime = True
    # Optimization: Check only up to square root of n
    while x * x <= n: # (optimised so that it checks only until the square root of n) If n=31 and x>5, x*x is more than 31 and not useful to check anything beyond that, if it is still not divisible then it would definitely be a prime number as 6*6=36>31 and if anything below 5 was divisible by 31 then 31 wouldn't be a prime number
        if n % x == 0:
            print("No")
            is_prime = False
            break
        x = x + 1
    
    if is_prime:
        print("Yes")