from abc import ABC, abstractmethod # abstractmethod is decorator and ABC is
class Polygon(ABC): # Creates an abstract class
    def __init__(self,color):
        self.color=color
    @abstractmethod # creates abstract method
    def printsides(self):
        pass # creates empty methods
    def printcolor(self):
        print(self.color)

class Triangle(Polygon):
    def __init__(self,color):
        super().__init__(color)
    def printsides(self):
        print("There are 3 sides")

p=Triangle("red")
p.printsides()
p.printcolor()





class Shape(ABC):

    def __init__(self, c):
        self.color = c  # Assign color attribute

    def get_color(self):
        return self.color

    @abstractmethod
    def get_area(self):
        pass  # Abstract method, to be implemented by subclass


# Square class that extends Shape
class Square(Shape):

    def __init__(self, c, side):
        super().__init__(c)  # Call the constructor of Shape to set color
        self.side = side

    def get_area(self):
        return self.side * self.side  # Area of the square

s = Square("blue", 5)
print(s.get_area())  # Output: 25
print(s.get_color())  # Output: blue

