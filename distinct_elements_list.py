# Method 1

def distinct(l):
    res=1
    for i in range(1,len(l)):
        if l[i] not in l[0:i]:
            res=res+1
    return res

# OR method 2

def distinct2(l):
    s=set(l) #set should only have all elements existing only once, and wont take duplication of one list item again, the length again gives number of distinct elements
    return len(s)


