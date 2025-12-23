s = input("Enter the string:")
rev=""
for i in s:
    rev=i+rev
print(rev)

'''Example input=abcd
Loop 1. i=a then rev=a
Loop 2. i=b then rev=ba
Loop 3. i=c then rev=cba
Loop 4. i=d then rev=dcba'''

#or shortcut method

'''s=input("Enter the string:")
print(s[::-1])'''

''' string slicing involves s[x:y:z] giving substring from index x to y in subs or increment order of z'''
