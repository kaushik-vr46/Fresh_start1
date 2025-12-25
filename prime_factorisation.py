# Function to check if a number is prime
def isPrime(x):
    # Check divisibility from 2 to x-1
    for i in range(2, x):
        if x % i == 0:  # If divisible by any number, it's not prime
            return False
        else:  # If not divisible, it's prime
            return True

# Function to find and print all prime factors
def printPFactors(n):
    for i in range(2, n + 1):  # Check each number from 2 to n
        if isPrime(i):  # If number i is prime
            x = i  # Use it as a potential factor
        # Keep dividing n by this prime factor while possible
        while n % x == 0:
            print(i)  # Print the prime factor
            x = x * i  # Multiply to track powers of the prime

# Get number from user and print its prime factors
n = int(input("Enter the number n: "))
printPFactors(n)




