# --- Break Statement ---
# Exits the loop immediately when condition is met.
print("--- Break Loop ---")
i = 1
while i <= 5:
    if i == 3:
        break 
    print(i)
    i += 1


# --- Continue Statement ---
# Skips the rest of the code inside the loop for the current iteration.
print("\n--- Continue Loop ---")
l = [10, 16, 17, 18, 9, 15, 21, 13]
for x in l:
    if x % 5 == 0:
        continue 
    if x % 7 == 0:
        break
    print(x)
print("Bye")


# --- Nested Loops ---
# Example: Printing tables or traversing 2D lists.
print("\n--- Nested List Traversal ---")
ll = [[10, 20, 30], [40, 50, 60], [70, 80]]
for l in ll: # traverses to get list (l) from main list (ll)
    for x in l: # traverses list (l) to get individual list items x
        print(x, end=" ") # end is for the space between numbers
    print() # this is for new line for next table