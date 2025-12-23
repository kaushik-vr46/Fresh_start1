def isPrime(x): # checks if the number itself running in loop in next fn is prime or not
    for i in range(2,x):
        if x%i==0:
            return False
        else:
            return True
def printPFactors(n):
    for i in range(2,n+1):
        if isPrime(i):
            x=i
        while n%x==0:
            print(i)
            x=x*i

n=int(input("Enter the number n:"))
printPFactors(n)




