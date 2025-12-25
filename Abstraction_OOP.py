# Import required modules for abstract base classes
from abc import ABC, abstractmethod
# ABC: Abstract Base Class
# abstractmethod: decorator to create abstract methods

# --- First Example: Polygon Hierarchy ---

# Create abstract base class for Polygon
class Polygon(ABC):
    def __init__(self, color):
        self.color = color  # Store color attribute
    
    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def printsides(self):
        pass  # Empty body, no implementation
    
    # Concrete method: can be used by subclasses as is
    def printcolor(self):
        print(self.color)

# Concrete class that implements the abstract method
class Triangle(Polygon):
    def __init__(self, color):
        super().__init__(color)  # Call parent class constructor
    
    def printsides(self):
        print("There are 3 sides")

# Create Triangle object and use it
p = Triangle("red")
p.printsides()   # Output: There are 3 sides
p.printcolor()   # Output: red


# --- Second Example: Shape Hierarchy ---

# Abstract base class for shapes
class Shape(ABC):
    def __init__(self, c):
        self.color = c  # Assign color attribute

    def get_color(self):
        # Concrete method available to all subclasses
        return self.color

    @abstractmethod
    def get_area(self):
        # Abstract method: subclasses MUST implement this
        pass

# Concrete class that extends Shape
class Square(Shape):
    def __init__(self, c, side):
        super().__init__(c)  # Call parent constructor to set color
        self.side = side  # Store side length

    def get_area(self):
        # Implement the abstract method
        return self.side * self.side  # Calculate area

# Create and use Square object
s = Square("blue", 5)
print(s.get_area())   # Output: 25 (5*5)
print(s.get_color())  # Output: blue

