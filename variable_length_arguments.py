# Function demonstrating variable-length arguments using *args
def sum(*elements):  # '*' allows the function to accept any number of arguments
    res = 0  # Initialize sum to 0
    for x in elements:  # Iterate through all passed arguments
        res = res + x  # Add each argument to the sum
    return res  # Return the total sum

# Examples:
# sum(10, 20) would return 30
# sum(1, 2, 3, 4) would return 10
# sum(5) would return 5

# Alternative version with initial value:
'''
def sum(init_sum, *elements):
    # init_sum: first regular parameter (required)
    # *elements: variable number of additional arguments
    res = init_sum
    for x in elements:
        res = res + x
    return res

Examples:
sum(10, 20, 30) -> 10 + 20 + 30 = 60
sum(5, 1, 2, 3) -> 5 + 1 + 2 + 3 = 11
'''

