
def listsorted(l):
    i=1
    while i < len(l):
        if l[i] < l[i-1]:
            return False
        i=i+1
    return True

# OR (Method 2)

def listsorted2(l):
    sl=sorted(l) #sorts the list elements in ascending order so we can equate sl and l to find if they are same as they should to satisfy the condition
    if sl==l:
        return True
    else:
        return False

l=[9,8,7,6,5,4,3,2,1]
print(listsorted(l))
print(listsorted2(l))

