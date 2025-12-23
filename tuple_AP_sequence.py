def sequence(tup):
    ans = list(tup)
    d = tup[1] - tup[0]  # d = a1-a0
    for i in range(3): # prints the next 3 numbers after the last tuple element given (0,1,2)
        ans.append(ans[-1] + d)
    return tuple(ans)
