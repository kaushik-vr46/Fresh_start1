# --- Sets in Python ---
# Sets are unordered collections of unique elements.
s1 = {10, 20, 30}
print(f"Set s1: {s1}")

s2 = set([20, 30, 40])
print(f"Set s2: {s2}")

s3 = {}
print(f"Type of s3 (empty dict): {type(s3)}")  # Empty curly braces create a dict

s4 = set()
print(f"Type of s4 (empty set): {type(s4)}")
print(f"Sum of s1: {sum(s1)}")


# --- print() formatting ---
# Using 'end' to avoid newlines and 'sep' to specify separators.
print("welcome", end="") 
print("to GFG")

print("25", "08", "2020", sep="-") 


# --- input() handling ---
# input() always returns a string; type casting is needed for numbers.
name = input("Enter your name: ")
age_input = input("Enter your age: ")
age = int(age_input) 

print("Welcome", name, sep=" ")
print("Your age is", str(age), sep=" ")