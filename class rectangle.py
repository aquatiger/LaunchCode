"""
Create rectangle with idea of knowing 3 things: lower left, width, height

"""
import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def reflect(self, v, w):
        return  (v, -w)

    def slope(self, otherP):
        try:
            return (otherP.getY() / otherP.getX())
        except:
            return None

    def move(self, z, a):                   #These are units of measurement, not coordinates
        self.x += z
        self.y += a
        return (self.x, self.y)
        
    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

class Rectangle:
    """ Rectangle class to represent and manipulate rectangles. """

    def __init__ (self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def  getWidth(self):
        return self.w

    def getHeight(self):
        return self.h

    def xCoord(self):
        return self.x

    def yCoord(self):
        return self.y

    def area (self):
        return self.w*self.h

    def perimeter(self):
        return ((2*self.w)+(2*self.h))

    def transpose(self):
        a = self.h
        b = self.w
        self.h = self.h-self.h + b
        self.w = self.w-self.w + a

    def diagonal(self):
        return math.sqrt((self.h ** 2) + (self.w ** 2))

    def contains(self, x2, y2):
        """Determines if a point falls inside a rectangle"""
        if x2 >= self.x and x2 < (self.x + self.w):
            if y2 >= self.y and y2 < (self.y+self.h):
                return True
            else:
                return False

r = Rectangle(10, 3, 5, 10)
print(r.xCoord())
print(r.yCoord())
print(r.area())
print(r.perimeter())
print(r.getWidth())
print(r.getHeight())
r.transpose()
print(r.getWidth())
print(r.getHeight())
print(r.diagonal())
print(r.contains(16,5))
