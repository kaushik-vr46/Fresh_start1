''' 17's binary is 16+1
i.e. 1/16 ; 0/8 ; 0/4 ; 0/2 ; 1/1
i.e. 10001
for 12 = 8+4
1/8 ; 1/4 ; 0/2 ; 1/1
i.e. 1101
for 15 = 8+4+2+1
1/8 ; 1/4 ; 1/2 ; 1/1
i.e. 1111'''
def decToBinary(n):
    if n==0:
        return "0"
    res=""
    while n>0:
        res = res+str(n%2) #the number can only be attached/concatenated to the end of res only if it is converted to a string and concatenated.
        n=n//2
    return res[::-1] #this is done as the numbers are attached to the end and we need a reverse of res to get the correct order of the binary number

#OR (built-in function method)

def decToBin(n):
    res=bin(n)
    return res[2:] #as the bin function will return a value that starts with '0b' indicating it as binary so we need to eliminate it

