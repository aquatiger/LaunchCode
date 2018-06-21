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

p = Point(3, 3)
q = Point(0, 7)
print(p.getX())
print(p.getY())
print(q.reflect(3, -5))
print(q.slope(q))
print(p.distanceFromPoint(q))
print(p.move(0, 7))
