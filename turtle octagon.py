
import turtle

wn = turtle.Screen()
wn.bgcolor("darkgreen")

hadir = turtle.Turtle()
hadir.color("yellow")

def nonFruitful(someturtle, somesides, somesize):
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360/somesides)
        
        
nonFruitful(hadir, 8, 50)

wn.exitonclick()
