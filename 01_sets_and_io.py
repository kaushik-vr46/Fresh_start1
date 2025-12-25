# --- Sets in Python ---
# Sets are unordered collections of unique elements (no duplicates).
s1 = {10, 20, 30}  # Create a set with curly braces
print(f"Set s1: {s1}")

s2 = set([20, 30, 40])  # Create a set from a list
print(f"Set s2: {s2}")

s3 = {}  # Empty curly braces create a dictionary, NOT a set
print(f"Type of s3 (empty dict): {type(s3)}")

s4 = set()  # Use set() to create an empty set
print(f"Type of s4 (empty set): {type(s4)}")
print(f"Sum of s1: {sum(s1)}")  # Calculate sum of all elements


# --- print() formatting ---
# 'end' parameter: Changes what comes after the output (default is newline)
# 'sep' parameter: Changes the separator between arguments (default is space)
print("welcome", end="")  # No newline after this
print("to GFG")  # Prints immediately after previous

print("25", "08", "2020", sep="-")  # Output: 25-08-2020 (dash separator)


# --- input() handling ---
# input() always returns a STRING, even for numeric input
# Type casting is needed to convert strings to numbers
name = input("Enter your name: ")  # Get name as string
age_input = input("Enter your age: ")  # Get age as string
age = int(age_input)  # Convert string to integer

print("Welcome", name, sep=" ")  # Print with space separator
print("Your age is", str(age), sep=" ")  # Convert age back to string for printing