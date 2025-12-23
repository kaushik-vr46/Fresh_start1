def average(l):
    sum=0
    for i in l:
        sum=sum+i
    n=len(l)
    return sum/n

# OR (Simple pre-defined function method)

def average2(l):
    return sum(l)/len(l)

l=[1,2,3,4,5,6,7,8,9]
print(average2(l))
print(average(l))

