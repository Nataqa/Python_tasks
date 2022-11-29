import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getWidth(self):
        return self.width

    def getHeigth(self):
        return self.height

    def getArea(self):
        return self.width * self.height

class Square:
    def __init__(self, side):
        self.side = side
    def getAreaSquare(self):
        return self.side**2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getCircleArea(self):
        return math.pi * self.radius**2