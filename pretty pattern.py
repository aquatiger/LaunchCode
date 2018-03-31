
import turtle

wn = turtle.Screen()
wn.bgcolor("yellow")

hadir = turtle.Turtle()
hadir.color("darkgreen")
hadir.speed(0)

def prettyPattern(t, size, numberOfSides):
    for i in range(numberOfSides):
        for i in range(4):
            t.forward(size)
            t.left(90)
    t.pu()
    t.right(360/numberOfSides)
    t.pd()
    
for i in range(10):
    prettyPattern(hadir, 100, 10)
    hadir.left(numberOfSides/360)
    
wn.exitonclick()
