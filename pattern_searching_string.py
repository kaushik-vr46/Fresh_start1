txt=input("Enter the text:")
pat=input("Enter the pattern:")
pos = txt.find(pat)
while pos>=0:
    print(pos)
    pos=txt.find(pat,pos+1) #to search the txt again to find if there is another iteration of pat in txt


