# Get number of rows from user
n = int(input("Enter number of rows for patterns: "))

# --- Square Pattern ---
# Prints n×n grid of stars
print("\n--- Square Pattern ---")
for i in range(n):  # Loop n times for rows
    for j in range(n):  # Loop n times for columns
        print("*", end=" ")  # Print star with space
    print()  # Newline after each row

# --- Triangle Pattern ---
# Prints increasing triangle (1 star, 2 stars, 3 stars, ...)
print("\n--- Triangle Pattern ---")
for i in range(n):  # Loop n times for rows
    for j in range(i + 1):  # Print (i+1) stars: row 1 has 1 star, row 2 has 2 stars, etc.
        print("*", end=" ")
    print()  # Newline after each row

# --- Inverted Triangle ---
# Prints decreasing triangle (n stars, n-1 stars, ...)
print("\n--- Inverted Triangle ---")
for i in range(n):  # Loop n times for rows
    for j in range(n - i):  # Print (n-i) stars: decreases each row
        print("*", end=" ")
    print()  # Newline after each row

# --- Pyramid Pattern ---
# Prints centered pyramid with leading spaces
print("\n--- Pyramid Pattern ---")
for i in range(n):  # Loop n times for rows
    # Print leading spaces for centering
    for j in range(n - i - 1):  # (n-i-1) spaces to center the row
        print(" ", end=" ")
    # Print stars (2*i+1): row 0 has 1 star, row 1 has 3 stars, row 2 has 5 stars, etc.
    for k in range(2 * i + 1):
        print("*", end=" ")
    print()  # Newline after each row