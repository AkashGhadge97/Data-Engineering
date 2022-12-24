#Function Ovrriding
from math import pi

class Shape:
    def __init__(self,name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        pass

    def whichShape(self):
        print(self.name)

class Square(Shape):

    def __init__(self, name, length):
        super().__init__(name)
        self.length = length
    
    def area(self):
        print(self.length**2)

    def fact(self):
        print("All the sides of square are of same length")

class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        print(pi*(self.radius**2))

    def fact(self):
        print("Circle has radius")

sq = Square("Square",  5)
cr = Circle("Circle", 14)

sq.area()
cr.area()

sq.fact()
cr.fact()

sq.whichShape()
cr.whichShape()