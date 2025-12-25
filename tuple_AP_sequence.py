# Function to extend an arithmetic progression (AP) sequence
def sequence(tup):
    # Convert tuple to list so we can add elements
    ans = list(tup)
    
    # Calculate the common difference (d) between consecutive terms
    # Example: For (2, 5, 8), d = 5-2 = 3
    d = tup[1] - tup[0]
    
    # Generate and append the next 3 terms in the sequence
    for i in range(3):  # Add 3 more terms
        # ans[-1] gets the last element, add d to get the next term in AP
        ans.append(ans[-1] + d)
    
    # Convert list back to tuple and return
    return tuple(ans)

'''
ARITHMETIC PROGRESSION (AP) EXAMPLE:
For input tuple (1, 2, 3):
- Common difference d = 2-1 = 1
- Next terms: 3+1=4, 4+1=5, 5+1=6
- Output: (1, 2, 3, 4, 5, 6)
'''
