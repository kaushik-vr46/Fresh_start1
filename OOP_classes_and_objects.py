# --- Complex Number Class ---
class Complex:
    # Constructor: initializes the object with real and imaginary parts
    def __init__(self, real, imag):
        # Create instance attributes (member variables)
        self.real = real  # Store real part
        self.imag = imag  # Store imaginary part
    
    # Method to print complex number in standard form
    def print(self):
        # Combine real and imaginary parts as "real+i*imag"
        print(str(self.real) + "+i" + str(self.imag))
    
    # Method to add another complex number to this one
    def add(self, c):
        # 'c' is another Complex object
        self.real += c.real  # Add real parts
        self.imag += c.imag  # Add imaginary parts

# Create first complex number: 10 + 20i
c1 = Complex(10, 20)
c1.print()  # Output: 10+i20

# Create second complex number: 20 + 30i
c2 = Complex(20, 30)

# Add c2 to c1 (c1 now becomes 30 + 50i)
c1.add(c2)  # c1 is passed as 'self', c2 is passed as 'c'
c1.print()  # Output: 30+i50

# --- Class and Instance Attributes in Python ---
# Instance attributes: unique to each object (defined in __init__)
# Class attributes: shared by all objects of the class (defined outside __init__)
