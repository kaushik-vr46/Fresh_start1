'''110's decimal is 6
i.e. 1/4 ; 1/2 ; 0/1 that indicates 4+2 is 6

for 10001 it will be
1/16 ; 0/8 ; 0/4 ; 0/2 ; 1/1 which is 16+1 = 17'''

def binToDec(b):
    res=0
    p=1
    for x in reversed(b):
        res=res+int(x)*p #start from the rightmost number in the binary by taking it as string, and then making it decimal and multiplying if it has a non zero value
        p=p*2 #to multiply as we move leftwards the powers of 2 to get whether the dec value to add exists or not
    return res

#OR (in-built function)

def binToDec2(b):
    res=int(b,2) #giving a base as 2 to multiply the binary by powers of 2 for dec to bin conversion
    return res

n=input()
print(binToDec2(n))
print(binToDec(n))
