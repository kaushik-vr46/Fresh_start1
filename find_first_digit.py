# Function to find the first (leftmost) digit of a number
def firstdigit(x):
    # Keep dividing by 10 until x becomes single digit (less than 10)
    # Examples: 12345 -> 1234 -> 123 -> 12 -> 1
    while x >= 10:
        x = x // 10  # Integer division removes the last digit
    return x  # When x < 10, we have the first digit

# Get number from user and print its first digit
x = int(input("Enter the number: "))
print(firstdigit(x))