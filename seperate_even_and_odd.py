def sepevenandodd(l):
    even=[]
    odd=[]
    for e in l:
        if e%2==0: even.append(e) # adds e to even if e is even
        else: odd.append(e) #vice versa0
    return even, odd

l=[1,2,3,4,5,6,7,8,9]
even,odd = sepevenandodd(l)
print(even)
print(odd)

