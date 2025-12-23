def firstdigit(x):
    while x>=10:
        x=x//10
    return x

x=int(input("Enter the number:"))
print(firstdigit(x))