# --- Break Statement ---
# Exits the loop immediately when the condition is met.
# Skips all remaining iterations of the loop.
print("--- Break Loop ---")
i = 1
while i <= 5:
    if i == 3:  # When i equals 3
        break  # Exit the loop completely
    print(i)  # Only prints 1, 2 (stops at 3)
    i += 1


# --- Continue Statement ---
# Skips the rest of the current iteration and jumps to the next one.
# Does NOT exit the loop (unlike break).
print("\n--- Continue Loop ---")
l = [10, 16, 17, 18, 9, 15, 21, 13]
for x in l:
    if x % 5 == 0:  # If divisible by 5
        continue  # Skip to next iteration (doesn't print)
    if x % 7 == 0:  # If divisible by 7
        break  # Exit loop completely
    print(x)  # Prints numbers that passed both conditions
print("Bye")


# --- Nested Loops ---
# Loops within loops: useful for 2D data structures (lists of lists)
# Outer loop iterates through each sublist
# Inner loop iterates through each element in the sublist
print("\n--- Nested List Traversal ---")
ll = [[10, 20, 30], [40, 50, 60], [70, 80]]  # 2D list (list of lists)
for l in ll:  # Outer loop: get each sublist (l) from main list (ll)
    for x in l:  # Inner loop: get each element (x) from current sublist (l)
        print(x, end=" ")  # Print element with space (no newline)
    print()  # Print newline after each sublist