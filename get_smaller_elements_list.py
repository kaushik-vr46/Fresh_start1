# --- Method 1: Using a loop to build result list ---
def getsmaller(l, x):
    res = []  # Empty list to store smaller elements
    for e in l:  # Iterate through each element in list l
        if e < x:  # Check if element is smaller than x
            res.append(e)  # Add it to result list
    return res  # Return list of elements smaller than x

# --- Method 2: Using list comprehension (more concise) ---
def getsmall(l, x):
    # Shorter syntax: [expression for item in list if condition]
    return [e for e in l if e < x]

# Test with sample data
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 6
# Find all elements smaller than 6
print(getsmall(l, x))  # Output: [1, 2, 3, 4, 5]