n = int(input("Enter number of rows for patterns: "))

#square pattern in py

print("\n--- Square Pattern ---")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

#triangle pattern

print("\n--- Triangle Pattern ---")
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

#inverted triangle

print("\n--- Inverted Triangle ---")
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

#pyramid pattern

print("\n--- Pyramid Pattern ---")
for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end=" ") # Note: Adjusted space for alignment
    # Print stars
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()