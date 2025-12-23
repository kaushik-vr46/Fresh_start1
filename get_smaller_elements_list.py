def getsmaller(l,x):
    res=[]
    for e in l:
        if e<l:
            res.append(e) # prints smaller elements than given x by user from the list given l only
    return res

# or (alternative with list comprehension method)

def getsmall(l,x):
    return [e for e in l if e<x]

l=[1,2,3,4,5,6,7,8,9]
x=6
print(getsmall(l,x))