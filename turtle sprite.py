
import turtle
wn = turtle.Screen()

hadir = turtle.Turtle()
hadir.speed(0)

def drawSprite(t, legs, length):
    for i in range(legs):
        t.forward(length)
        t.backward(length)
        t.left(360/legs)


drawSprite(hadir, 10, 100)

wn.exitonclick()
