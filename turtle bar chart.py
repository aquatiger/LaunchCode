
import turtle

wn = turtle.Screen()

hadir = turtle.Turtle()
hadir.speed(0)
##hadir.color("blue")
##hadir.fillcolor("orange")

def barChart(t, xs, distance):
    for i in xs:
        drawBar(hadir, i)
    hadir.backward(numbars * 40) + (border * numbars)

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape



xs = [48, 117, 200, 240, 160, 260, 220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

barChart(hadir, xs, 10)

wn.exitonclick()
