# Function to separate even and odd numbers from a list
def sepevenandodd(l):
    even = []  # List to store even numbers
    odd = []  # List to store odd numbers
    for e in l:  # Iterate through each element
        if e % 2 == 0:  # Check if element is even (divisible by 2)
            even.append(e)  # Add to even list
        else:  # Otherwise it's odd
            odd.append(e)  # Add to odd list
    return even, odd  # Return both lists as a tuple

# Test data
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Call function and unpack results
even, odd = sepevenandodd(l)

# Print results
print(even)  # Output: [2, 4, 6, 8]
print(odd)   # Output: [1, 3, 5, 7, 9]

