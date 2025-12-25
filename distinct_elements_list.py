# --- Method 1: Manual checking using slicing ---
def distinct(l):
    res = 1  # Start with count of 1 (first element is always distinct)
    for i in range(1, len(l)):  # Check each element starting from index 1
        if l[i] not in l[0:i]:  # Check if current element exists in previous elements
            res = res + 1  # If not found, it's a new distinct element
    return res  # Return count of distinct elements

# --- Method 2: Using set (Simpler and faster) ---
def distinct2(l):
    # Sets automatically remove duplicates and keep only unique elements
    # len(s) gives the count of distinct elements
    s = set(l)
    return len(s)


