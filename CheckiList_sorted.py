
# --- Method 1: Manual comparison approach ---
def listsorted(l):
    i = 1  # Start from index 1 (second element)
    while i < len(l):  # Loop through the entire list
        if l[i] < l[i-1]:  # Check if current element is smaller than previous
            return False  # If yes, list is NOT sorted in ascending order
        i = i + 1  # Move to next element
    return True  # If all comparisons pass, list IS sorted

# --- Method 2: Using built-in sorted() function ---
def listsorted2(l):
    sl = sorted(l)  # Create a new sorted version of the list in ascending order
    # Compare original list with sorted list
    if sl == l:  # If they are identical, the original was already sorted
        return True
    else:
        return False

# Test data: Unsorted list in descending order
l = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Print results using both methods
print(listsorted(l))   # Output: False (list is not sorted)
print(listsorted2(l))  # Output: False (list is not sorted)

