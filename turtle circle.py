import turtle

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.pd()
        t.forward(sideLength)
        t.left(turnAngle)

def drawCircle(anyTurtle, radius, starting):
    anyTurtle.pu()
    anyTurtle.goto(0, -radius)
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)
    

wn = turtle.Screen()
wheel = turtle.Turtle()
wheel.speed(0)
drawCircle(wheel, 50, 0)

wn.exitonclick()
