
import turtle
wn = turtle.Screen()

hadir = turtle.Turtle()
hadir.speed(7)


def drawSquare(t):
    for i in range(4):
        t.forward(100)
        t.left(90)
        drawSprite(hadir, 5, 30)

def drawSprite(t, legs, length):
    for i in range(legs):
        t.forward(length)
        t.backward(length)
        t.left(360/legs)

drawSquare(hadir)
drawSprite(hadir, 5, 30)

wn.exitonclick()
