def sum(*elements): # '*' is the variable length argument indicator
    res=0
    for x in elements:
        res=res+x
        return res

#print(sum(10,20))

#or

'''def sum(init_sum, *elements): # '*' is the variable lengthn argument indicator
    res=init_sum
    for x in elements:
        res=res+x
        return res'''

