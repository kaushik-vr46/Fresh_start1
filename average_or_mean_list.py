# --- Method 1: Manual approach to calculate average ---
def average(l):
    sum=0  # Initialize sum to 0
    for i in l:  # Iterate through each element in the list
        sum=sum+i  # Add each element to the running sum
    n=len(l)  # Get the total count of elements in the list
    return sum/n  # Return the average (sum divided by count)

# --- Method 2: Using built-in functions (Simpler and cleaner) ---
def average2(l):
    # sum(l) calculates the total, len(l) gets the count, division gives the average
    return sum(l)/len(l)

# Test data: List of numbers from 1 to 9
l=[1,2,3,4,5,6,7,8,9]

# Print average using both methods
print(average2(l))  # Output: 5.0 (using built-in functions)
print(average(l))  # Output: 5.0 (using manual loop)

