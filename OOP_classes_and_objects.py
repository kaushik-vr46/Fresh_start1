class Complex: #
    def __init__(self, real, imag):
        self.real = real # self creates a member with the parameters self and imag that user enters
        self.imag = imag
    def print(self):
        print(str(self.real)+"+i"+str(self.imag)) # prints the string format of the member real and imag
    def add(self,c):
        self.real+=c.real
        self.imag+=c.imag

c1=Complex(10,20)
c1.print()
c2=Complex(20,30)
c1.add(c2) # c1 is passed as 1st parameter self and c2 is passed as c and result becomes 30,50 as self and c objects are asked to be added\
c1.print()

# Class and instance attributes in python
